import grpc
from google.oauth2 import id_token
from google.auth.transport import requests


def _unary_unary_rpc_terminator(code, details):
    def terminate(ignored_request, context):
        context.abort(code, details)

    return grpc.unary_unary_rpc_method_handler(terminate)


class AuthInterceptor(grpc.ServerInterceptor):
    """
    Interceptor to verify that client calls are authenticated
    """
    def __init__(self, code, details, creds):
        self._creds = creds
        self._terminator = _unary_unary_rpc_terminator(code, details)

    def intercept_service(self, continuation, handler_call_details):
        """
        Intercepts incoming RPCs before handing them over to a handler.

        Args:
            continuation: A function that takes a HandlerCallDetails and
            proceeds to invoke the next interceptor in the chain, if any,
            or the RPC handler lookup logic, with the call details passed
            as an argument, and returns an RpcMethodHandler instance if
            the RPC is considered serviced, or None otherwise.
            handler_call_details: A HandlerCallDetails describing the RPC.

        Returns:
            An RpcMethodHandler with which the RPC may be serviced if the
            interceptor chooses to service this RPC, or None otherwise.
        """
        metadata = dict(handler_call_details.invocation_metadata)
        if 'id_token' not in metadata:
            return self._terminator
        token = metadata['id_token']

        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(),
                                                  self._creds.get_client_id())
            if idinfo['iss'] not in [
                    'accounts.google.com', 'https://accounts.google.com'
            ]:
                raise ValueError('Wrong issuer.')
            user_email = idinfo['email']
        except ValueError:
            return self._terminator

        verified = self._creds.verify_user(user_email)
        if verified:
            return continuation(handler_call_details)
        return self._terminator
