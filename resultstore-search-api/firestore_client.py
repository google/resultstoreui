import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FireStoreClient():
    """ Resultstore search's firestore client"""
    def __init__(self, project_id):
        """ Initialize the client """
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
            'projectId': project_id,
        })

        self.db = firestore.client()

    def add_tool_tag(self, tool_tag):
        """
        Add the provided tool_tags to firestores' resultstore_tools collection
        
        Args:
            tool_tag (str): Tool tag to be added
        """
        col_ref = self.db.collection(u'resultstore_tools')
        col_ref.add({u'name': tool_tag})

    def get_tools(self):
        """
        Queries resultstore_tools collection from firestore and returns
        a list of tool names

        returns (Seq[str])
        """
        tools_ref = self.db.collection(u'resultstore_tools')
        docs = tools_ref.stream()
        tools = []
        for doc in docs:
            tools.append(doc.get('name'))
        return tools
