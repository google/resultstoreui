from concurrent import futures
from resultstoreapi.cloud.devtools.resultstore_v2.proto import (
    resultstore_download_pb2_grpc, )
from resultstoresearchapi import (
    resultstore_download_pb2_grpc as resultstoresearch_download_pb2_grpc,
    resultstore_download_pb2 as resultstoresearch_download_pb2,
)
from credentials.credentials import Credentials
from resultstore_proxy_server import ProxyServer
from firestore.firestore_client import FireStoreClient
from bigstore.bigstore_client import BigstoreClient
from auth.auth_interceptor import AuthInterceptor
import logging
import grpc
import sys


def serve():
    creds = Credentials()
    fs = FireStoreClient(creds.get_project_id())
    bs = BigstoreClient(creds)
    auth_interceptor = AuthInterceptor(grpc.StatusCode.UNAUTHENTICATED,
                                       'Invalid Authorization', creds)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         interceptors=(auth_interceptor, ))
    with creds.create_secure_channel(creds.get_destination_sever()) as channel:
        proxy_server = ProxyServer(channel, fs, bs)
        resultstoresearch_download_pb2_grpc.add_ResultStoreDownloadServicer_to_server(
            proxy_server, server)
        server.add_insecure_port(creds.get_port())
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    serve()
