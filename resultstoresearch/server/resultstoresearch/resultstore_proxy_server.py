from resultstoreapi.cloud.devtools.resultstore_v2.proto import (
    resultstore_download_pb2_grpc, resultstore_download_pb2, resultstore_file_download_pb2, resultstore_file_download_pb2_grpc)
from resultstoresearchapi import (
    resultstore_download_pb2_grpc as resultstoresearch_download_pb2_grpc,
    resultstore_download_pb2 as resultstoresearch_download_pb2,
)
from utils.proxy_server_utils import (configure_grpc_error, filter_tool,
                                      update_tools_list, convert_files,
                                      convert_invocation, parse_tests, convert_actions,
                                      convert_invocations)
from google.cloud import storage
import logging
import grpc

GET_TEST_CASES_FIELD_MASK = 'next_page_token,actions.test_action,actions.name,actions.test_action.test_suite,actions.id'

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class ProxyServer(
        resultstoresearch_download_pb2_grpc.ResultStoreDownloadServicer):
    """
    Server that proxies requests to the search api forward to resultstore
    """

    def __init__(self, channel, fs, bs):
        """
        Initialize the Proxy Server

        Args:
            channel (grpc.Channel): Channel used to make requests to destination server
            fs (FireStoreClient): Client for firestore
        """
        self.channel = channel
        self.fs = fs
        self.bs = bs

    def SearchInvocations(self, request, context):
        """
        Proxies the SearchInvocations gRPC call forward

        Args:
            request (SearchInvocationsRequest): The search request
            context (grpc.Context)

        Returns:
            SearchInvocationsResponse
        """
        _LOGGER.info('Received request: %s', request)
        new_request = resultstore_download_pb2.SearchInvocationsRequest(
            query=request.query,
            project_id=request.project_id,
            page_size=request.page_size,
            page_token=request.page_token,
        )
        return self._search_helper(new_request, request.tool, context)

    def GetInvocation(self, request, context):
        """
        Proxies the GetInvocation gRPC call forward

        Args:
            request (GetInvocationRequest): The get request
            context (grpc.Context)

        Returns:
            An invocation
        """
        _LOGGER.info('Received request: %s', request)
        new_request = resultstore_download_pb2.GetInvocationRequest(
            name=request.name)
        metadata = context.invocation_metadata()
        stub = resultstore_download_pb2_grpc.ResultStoreDownloadStub(
            self.channel)
        try:
            response = stub.GetInvocation(new_request, metadata=metadata)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            configure_grpc_error(context, rpc_error)
            return resultstoresearch_download_pb2.GetInvocationRequest()
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def GetFile(self, request, context):
        """
        Proxies the GetFile gRPC call forward

        Args:
            request (GetFileRequest): The get request
            context (grpc.Context)

        Returns:
            GetFileResponse
        """
        _LOGGER.info('Received request: %s', request)
        new_request = resultstore_file_download_pb2.GetFileRequest(
            uri='file/'+request.uri,
            read_offset=request.read_offset,
            read_limit=request.read_limit,
            archive_entry=request.archive_entry,
        )
        metadata = context.invocation_metadata()
        stub = resultstore_file_download_pb2_grpc.ResultStoreFileDownloadStub(
            self.channel
        )
        try:
            responses = stub.GetFile(new_request, metadata=metadata)
            for response in responses:
                yield response
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            configure_grpc_error(context, rpc_error)
            return resultstore_file_download_pb2.GetFileResponse()

    def ListTargets(self, request, context):
        _LOGGER.info('Received request: %s', request)
        metadata = context.invocation_metadata()
        new_request = resultstore_download_pb2.ListTargetsRequest(
            page_token=request.page_token,
            page_size=request.page_size,
            parent=request.parent)
        stub = resultstore_download_pb2_grpc.ResultStoreDownloadStub(
            self.channel)
        try:
            response = stub.ListTargets(new_request, metadata=metadata)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            configure_grpc_error(context, rpc_error)
            return resultstore_download_pb2.ListTargetsResponse()
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def ListTargetSubFiles(self, request, context):
        """
        Aggregates a list of ConfiguredTarget and Action files under a
        given parent Target

        Args:
            request (ListTargetSubFilesRequest): The request
            context (grpc.Context)

        Returns:
            ListTargetSubFilesResponse
        """
        _LOGGER.info('Received request: %s', request)
        files = []
        new_request = resultstore_download_pb2.ListConfiguredTargetsRequest(
            parent='invocations/30136a0c-a2a8-47f5-b771-709c40f385b9/targets/3bc60ba6-0dd1-43cc-8f49-668e67cebd58')
        stub = resultstore_download_pb2_grpc.ResultStoreDownloadStub(
            self.channel)
        metadata = [
            ('x-goog-fieldmask',
             'next_page_token,configured_targets.files,configured_targets.name')
        ]
        try:
            response = stub.ListConfiguredTargets(
                new_request, metadata=metadata)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            configure_grpc_error(context, rpc_error)
            return resultstoresearch_download_pb2.ListTargetSubFilesResponse()
        else:
            _LOGGER.info('Received message: %s', response)
            for configured_target in response.configured_targets:
                files += convert_files(configured_target.files)

        metadata = [
            ('x-goog-fieldmask',
             'next_page_token,actions.files,actions.name')
        ]
        try:
            for configured_target in response.configured_targets:
                new_request = resultstore_download_pb2.ListActionsRequest(
                    parent=configured_target.name)
                response = stub.ListActions(new_request, metadata=metadata)
                for action in response.actions:
                    files += convert_files(action.files)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            configure_grpc_error(context, rpc_error)
            return resultstoresearch_download_pb2.ListTargetSubFilesResponse()
        return resultstoresearch_download_pb2.ListTargetSubFilesResponse(files=files)

    def GetInitialState(self, request, context):
        """
        Gets the initial state of the client

        Args:
            request (GetInitialStateRequest): The initial state request
            context (grpc.Context)

        Returns:
            GetInitialStateResponse
        """
        return resultstoresearch_download_pb2.GetInitialStateResponse(
            tools_list=self.fs.get_tools())

    def DownloadFile(self, request, context):
        """
        Attempts to download the requested file from bigstore

        Args:
            request (DownloadFileRequest): The request
            context (grpc.Context)

        Returns:
            DownloadFileResponse
        """
        _LOGGER.info('Received request: %s', request)
        try:
            file_data = self.bs.get_file_blob(request.file_name)
        except Exception:
            context.set_details('Unable to find requested file')
            context.set_code(5)
            return resultstoresearch_download_pb2.DownloadFileResponse()
        else:
            return resultstoresearch_download_pb2.DownloadFileResponse(file_data=file_data)

    def GetTestCases(self, request, context):
        _LOGGER.info('Received request: %s', request)
        invocations = convert_invocations(request.invocations)
        page_token = request.page_token
        first_request = len(invocations) == 0
        while (first_request or page_token != ''):
            first_request = False
            new_request = resultstore_download_pb2.SearchInvocationsRequest(
                query=request.query,
                project_id=request.project_id,
                page_size=request.page_size,
                page_token=page_token,
            )
            response = self._search_helper(new_request, request.tool, context)
            invocations += response.invocations
            page_token = response.next_page_token

        page_token = ''
        stub = resultstore_download_pb2_grpc.ResultStoreDownloadStub(
            self.channel)
        metadata = [
            ('x-goog-fieldmask', GET_TEST_CASES_FIELD_MASK)]

        invocation_tests = []

        for invocation in invocations:
            first_request = True
            action_parent = '{}/targets/-/configuredTargets/-'.format(
                invocation.name)
            while page_token != '' or first_request:
                first_request = False
                list_actions_request = resultstore_download_pb2.ListActionsRequest(
                    parent=action_parent,
                    page_size=200,
                    page_token=page_token
                )
                list_actions_response = stub.ListActions(
                    list_actions_request, metadata=metadata)
                actions = list_actions_response.actions
                new_actions = convert_actions(actions)
                page_token = list_actions_response.next_page_token
                invocation_test = parse_tests(
                    invocation, new_actions)
                invocation_tests.append(invocation_test)
        return resultstoresearch_download_pb2.GetTestCasesResponse(
            invocation_tests=invocation_tests
        )

    def _search_helper(self, request, tool, context):
        metadata = context.invocation_metadata()
        stub = resultstore_download_pb2_grpc.ResultStoreDownloadStub(
            self.channel)
        try:
            response = stub.SearchInvocations(request, metadata=metadata)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            configure_grpc_error(context, rpc_error)
            return resultstoresearch_download_pb2.SearchInvocationsResponse()
        else:
            _LOGGER.info('Received message: %s', response)
            tools_list = self.fs.get_tools()
            tools_list = update_tools_list(response.invocations, tools_list,
                                           self.fs)
            filtered_invocations = filter_tool(response.invocations, tool)
            return resultstoresearch_download_pb2.SearchInvocationsResponse(
                invocations=filtered_invocations,
                next_page_token=response.next_page_token,
                tools_list=list(tools_list))
