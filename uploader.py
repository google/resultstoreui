import grpc
import argparse
# import resultstore_upload_pb2_grpc

_SERVER_ADDR_TEMPLATE = 'resultstore.googleapis.com'
_SIGNATURE_HEADER_KEY = 'x-signature'



class AuthGateway(grpc.AuthMetadataPlugin):

    def __call__(self, context, callback):
        """Implements authentication by passing metadata to a callback.

        Implementations of this method must not block.

        Args:
          context: An AuthMetadataContext providing information on the RPC that
            the plugin is being called to authenticate.
          callback: An AuthMetadataPluginCallback to be invoked either
            synchronously or asynchronously.
        """
        # Example AuthMetadataContext object:
        # AuthMetadataContext(
        #     service_url=u'https://localhost:50051/helloworld.Greeter',
        #     method_name=u'SayHello')
        signature = context.method_name[::-1]
        callback(((_SIGNATURE_HEADER_KEY, signature),), None)


# @contextlib.contextmanager
# def create_client_channel(addr):
#     # Call credential object will be invoked for every single RPC
#     call_credentials = grpc.metadata_call_credentials(AuthGateway(),
#                                                       name='auth gateway')
#     # Channel credential will be valid for the entire channel
#     channel_credential = grpc.ssl_channel_credentials(
#         _credentials.ROOT_CERTIFICATE)
#     # Combining channel credentials and call credentials together
#     composite_credentials = grpc.composite_channel_credentials(
#         channel_credential,
#         call_credentials,
#     )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port',
                        nargs='?',
                        type=int,
                        default=50051,
                        help='the address of server')
    args = parser.parse_args()
    print(args)
    # with create_client_channel(_SERVER_ADDR_TEMPLATE) as channel:
    #     stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(channel)
    #     response = stub.CreateInvocation

