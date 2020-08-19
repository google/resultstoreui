from resultstoresearch.resultstoresearchapi import (
    resultstore_download_pb2_grpc, resultstore_download_pb2)
from resultstoresearch.mock.mock_responses import (
    mock_search_invocations_response,
    mock_search_invocations_response_with_tools, mock_file, mock_target)
import logging
import grpc
import os


class MockProxyServer(resultstore_download_pb2_grpc.ResultStoreDownloadServicer
                      ):
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
        elif request.tool:
            return mock_search_invocations_response_with_tools()
        return mock_search_invocations_response()

    def ListTargets(self, request, context):
        """
        Mocks listing of targets for a given invocation

        Args:
            request (ListTargetsRequest): The ListTargets request
            context (grpc.Context)

        Returns:
            ListTargetsResponse
        """
        return [mock_target()]

    def ListTargetSubFiles(self, request, context):
        """
        Mocks listing of files under a given target

        Args:
            request (ListTargetSubFilesRequest): The ListTargetSubFiles request
            context (grpc.Context)

        Returns:
            ListTargetSubFilesResponse
        """
        return [mock_file(), mock_file()]

    def GetInitialState(self, request, context):
        """
        Gets the initial state of the client

        Args:
            request (GetInitialStateRequest): The initial state request
            context (grpc.Context)

        Returns:
            GetInitialStateResponse
        """
        return resultstore_download_pb2.GetInitialStateResponse(
            tools_list=['tool1', 'tool2'])

    def DownloadFile(self, request, context):
        """
        Mocks Downloading a file from bigstore

        Args:
            request (DownloadFileRequest): The DownloadFile request
            context (grpc.Context)

        Returns:
            DownloadFileResponse
        """
        with open('./mock/dummy_file.html', 'r') as file:
            data = file.read()
            return resultstore_download_pb2.DownloadFileResponse(
                file_data=data)
