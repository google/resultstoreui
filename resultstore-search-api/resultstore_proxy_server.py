from resultstoreapi.cloud.devtools.resultstore_v2.proto import (
    resultstore_download_pb2_grpc, resultstore_download_pb2, resultstore_file_download_pb2, resultstore_file_download_pb2_grpc)
from resultstoresearchapi import (
    resultstore_download_pb2_grpc as resultstoresearch_download_pb2_grpc,
    resultstore_download_pb2 as resultstoresearch_download_pb2,
)
from proxy_server_utils import (configure_grpc_error, filter_tool,
                                update_tools_list)
import logging
import grpc

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class ProxyServer(
        resultstoresearch_download_pb2_grpc.ResultStoreDownloadServicer):
    """
    Server that proxies requests to the search api forward to resultstore
    """

    def __init__(self, channel, fs):
        """
        Initialize the Proxy Server

        Args:
            channel (grpc.Channel): Channel used to make requests to destination server
            fs (FireStoreClient): Client for firestore
        """
        self.channel = channel
        self.fs = fs

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
        metadata = context.invocation_metadata()
        stub = resultstore_download_pb2_grpc.ResultStoreDownloadStub(
            self.channel)
        try:
            response = stub.SearchInvocations(new_request, metadata=metadata)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            configure_grpc_error(context, rpc_error)
            return resultstoresearch_download_pb2.SearchInvocationsResponse()
        else:
            _LOGGER.info('Received message: %s', response)
            tools_list = self.fs.get_tools()
            tools_list = update_tools_list(response.invocations, tools_list,
                                           self.fs)
            filtered_invocations = filter_tool(response.invocations,
                                               request.tool)
            return resultstoresearch_download_pb2.SearchInvocationsResponse(
                invocations=filtered_invocations,
                next_page_token=response.next_page_token,
                tools_list=list(tools_list))

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

    def GetFileRequest(self, request, context):
        _LOGGER.info('Received request: %s', request)
        new_request = resultstore_file_download_pb2.GetFileRequest(
            uri=request.uri,
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
