from google.cloud import storage
from google import auth


class BigstoreClient():
    def __init__(self, creds):
        self.client = storage.Client(
            credentials=auth.default(scopes=creds.get_scopes())[0],
            project=creds.get_project_id())
        self.bucket = self.client.get_bucket(creds.get_bucket_name())

    def get_file_blob(self, file_name):
        blob = self.bucket.blob(file_name)
        return blob.download_as_string()
