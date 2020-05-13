import os
import pathlib
from google import auth
from google.cloud import storage
from resultstoreapi.cloud.devtools.resultstore_v2.proto import (file_pb2)


class BigStoreClient(object):
    """ Client for BigStore"""

    def __init__(self, credentials, project_name, storage_dir, bucket_name):
        """
        Initialize BigStore Client

        Args:
            credentials (Credentials): credentials and scope for the client
            project_name (str): Porject name to connect to
            storage_dir (str): Specify directory to store uploaded files
            bucket_name (str): Bucket name to upload files to
        
        Return:
            List of files that were uploaded
        """
        self.credentials = credentials
        self.storage_dir = storage_dir
        self.bucket_name = bucket_name
        self.project_name = project_name

    def upload_files_to_bigstore(self, files):
        """
        Upload files to bigstore (aka google cloud storage).

        Args:
            files (Sequence[str]): list of file path names
            storage_dir (str): cloud storage dir where files should be saved
            bucket_name (str): cloud storage bucket name

        Returns:
            uploaded_files: A list of file_pb2.File() objects

        Raises:
            FileNotFoundError: if a file is missing.
        """
        prefix = self.storage_dir
        credentials = auth.default(scopes=self.credentials.get_scopes())

        # Create the client using the credentials and specifying a project ID.
        storage_client = storage.Client(credentials=credentials[0],
                                        project=self.project_name)
        bucket = storage_client.get_bucket(self.bucket_name)
        uploaded_files = []

        for pathname in files:
            path = pathlib.Path(pathname)
            if not path.exists() or not path.is_file():
                raise FileNotFoundError(pathname)
            filename = pathname.split('/')[-1]
            blob = bucket.blob(os.path.join(prefix, filename))
            blob.upload_from_filename(pathname)
            file_object = file_pb2.File(
                uid=filename,
                uri='googlefile:/bigstore/{}/{}'.format(
                    self.bucket_name, prefix + filename))
            uploaded_files.append(file_object)
        return uploaded_files
