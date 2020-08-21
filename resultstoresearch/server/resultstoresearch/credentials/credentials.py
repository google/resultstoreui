import contextlib
import os
from google import auth
from google.auth.transport import grpc as google_auth_transport_grpc
from google.auth.transport import requests as google_auth_transport_requests
from googleapiclient import discovery

BIGSTORE_SCOPES = [
    'https://www.googleapis.com/auth/devstorage.write_only',
]

RESULTSTORE_SCOPES = [
    "https://www.googleapis.com/auth/cloud-source-tools",
    "https://www.googleapis.com/auth/cloud-platform",
]

ALL_SCOPES = BIGSTORE_SCOPES + RESULTSTORE_SCOPES
RESULTSTORE_SEARCH_VIEW_ROLE = 'roles/cloudsourcetoolscore.developer'
PORT = '[::]:9090'


class Credentials():
    """
    Credentials container/helper for resultstoreui
    """

    def __init__(self):
        """
        Initialize Credentials

        Args:
            project_id: GCP project id
            client_id: GCP oauth client_id
        """
        self.channel = None
        self.scopes = ALL_SCOPES
        self.project_id = os.environ.get('PROJECT_ID')
        self.client_id = os.environ.get('CLIENT_ID')
        self.destination_sever = os.environ.get('RESULT_STORE_API_ENDPOINT')
        self.bigstore_bucket_name = os.environ.get('BUCKET_NAME')
        self.port = PORT

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

    def verify_user(self, email, version=1):
        """
        Verifies user by checking if they have the roles/cloudsourcetoolscore.developer
        in the currect gcp project

        Args:
            email (str): User email to check for authenticated
            version (int): cloudresourcemanager api version

        Returns:
            Boolean, true if verified, false if not verified
        """
        credentials, _ = auth.default(scopes=self.scopes)
        service = discovery.build('cloudresourcemanager',
                                  'v1',
                                  credentials=credentials)
        policy = (service.projects().getIamPolicy(
            resource=self.project_id,
            body={
                'options': {
                    'requestedPolicyVersion': version
                }
            },
        ).execute())
        try:
            roles = policy['bindings']
            index = self._index_of_role(roles, RESULTSTORE_SEARCH_VIEW_ROLE)
            if index == -1:
                return False
            if 'user:{}'.format(email) in roles[index]['members']:
                return True
            return False
        except:
            return False

    def get_client_id(self):
        """
        Returns:
            Application client_id
        """
        return self.client_id

    def get_project_id(self):
        """
        Returns:
            Application project_id
        """
        return self.project_id

    def get_destination_sever(self):
        """
        Returns:
            Application destination_sever
        """
        return self.destination_sever

    def get_port(self):
        """
        Returns:
            Application port
        """
        return self.port

    def get_bucket_name(self):
        return self.bigstore_bucket_name

    def _index_of_role(self, lst, role):
        """
        Find the index of the iap role in the list

        Args:
            lst (str): lst to be searched
            role (str): role that is being searched for

        Returns:
            Index of the role or -1 if it doesn't exist
        """
        for i, v in enumerate(lst):
            if v['role'] == role:
                return i
        return -1
