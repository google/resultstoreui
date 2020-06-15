from resultstoreapi.cloud.devtools.resultstore_v2.proto import (
    resultstore_download_pb2_grpc, resultstore_download_pb2)
from resultstoresearchapi import (
    resultstore_download_pb2_grpc as resultstoresearch_download_pb2_grpc,
    resultstore_download_pb2 as resultstoresearch_download_pb2,
)
from proxy_server_utils import configure_grpc_error
import logging
import grpc
from mock_responses import (
    mock_search_invocations_response
)

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class ProxyServer(
        resultstoresearch_download_pb2_grpc.ResultStoreDownloadServicer):
    """
    Server that proxies requests to the search api forward to resultstore
    """
    def __init__(self, channel):
        """
        Initialize the Proxy Server

        Args:
            channel (grpc.Channel): Channel used to make requests to destination server
        """
        self.channel = channel

    def SearchInvocations(self, request, context):
        """
        Proxies the SearchInvocations gRPC call forward
        
        Args:
            request (SearchInvocationsRequest): The search request
            context (grpc.Context)

        Returns:
            SearchInvocationsResponse
        """
        print('meme')
        return mock_search_invocations_response()
        _LOGGER.info('Received request: %s', request)
        new_request = resultstore_download_pb2.SearchInvocationsRequest(
            query=request.query,
            project_id=request.project_id,
            exact_match=request.exact_match,
            page_size=request.page_size,
            page_token=request.page_token,
            offset=request.offset,
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
            return response

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
