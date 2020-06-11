from resultstoresearchapi import (
    resultstore_download_pb2_grpc,
    resultstore_download_pb2
)
from mock_responses import (
    mock_search_invocations_response
)
import logging
import grpc

class MockProxyServer(
        resultstore_download_pb2_grpc.ResultStoreDownloadServicer):
    def SearchInvocations(self, request, context):
        """
        Proxies the SearchInvocations gRPC call forward

        Args:
            request (SearchInvocationsRequest): The search request
            context (grpc.Context)

        Returns:
            SearchInvocationsResponse
        """
        if request.query == 'incorrect query':
            context.set_details('Invalid query string')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return resultstore_download_pb2.SearchInvocationsResponse()
        return mock_search_invocations_response()
