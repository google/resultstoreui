import contextlib
from google import auth
from google.auth.transport import grpc as google_auth_transport_grpc
from google.auth.transport import requests as google_auth_transport_requests

BIGSTORE_SCOPES = [
    'https://www.googleapis.com/auth/devstorage.write_only',
]

RESULTSTORE_SCOPES = [
    "https://www.googleapis.com/auth/cloud-source-tools",
    "https://www.googleapis.com/auth/cloud-platform"
]

ALL_SCOPES = BIGSTORE_SCOPES + RESULTSTORE_SCOPES


class Credentials():
    """ Credentials container/helper for resultstoreui"""
    def __init__(self):
        """
        Initialize Credentials
        """
        self.channel = None
        self.scopes = ALL_SCOPES

    @contextlib.contextmanager
    def create_secure_channel(self, addr):
        """
        Creates a secure channel using GOOGLE_APPLICATION_CREDENTIALS from the
        users path

        Args:
            target (str): The host and port of the service
        
        Returns:
            A gRPC channel
        """
        credentials, _ = auth.default(scopes=self.scopes)
        request = google_auth_transport_requests.Request()
        channel = google_auth_transport_grpc.secure_authorized_channel(
            credentials, request, addr)
        self.channel = channel
        yield channel

    def get_active_channel(self):
        """Returns current active channel"""
        return self.channel

    def get_scopes(self):
        """Returns scopes"""
        return self.scopes
