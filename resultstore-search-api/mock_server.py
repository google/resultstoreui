import grpc
from concurrent import futures
from absl import (flags, app)
from resultstoresearchapi import (
    resultstore_download_pb2_grpc as resultstoresearch_download_pb2_grpc,
)
from mock_proxy import MockProxyServer

FLAGS = flags.FLAGS


def initialize_flags():
    flags.DEFINE_string('port', '[::]:9091', 'Server Port')


def serve(argv):
    mock_proxy_server = MockProxyServer()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    resultstoresearch_download_pb2_grpc.add_ResultStoreDownloadServicer_to_server(
        mock_proxy_server, server)
    server.add_insecure_port(FLAGS.port)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    initialize_flags()
    app.run(serve)
