from url_util import url_util
import requests
import json


class db_client:

    urlutil = url_util()

    """
    Function that creates a DB by the name provided if not present already.
    """
    def create_new_database(self, db_name, username, password):

        response = requests.put(self.urlutil.get_db_create_url(db_name, username),
                     auth=(username, password))

        return response

    """
    Function that creates a new document by the name provided if not present already.
    """
    def create_new_doc(self, db_name, doc_name, username, password):

        response = requests.put(self.urlutil.get_doc_create_url(db_name, username, doc_name),
                     auth=(username, password),
                     headers={"content-type": "application/json"},
                     data=json.dumps({"foo": "bar"}))

        return response

    """
    Function that gets and validates a new document by the name.
    """
    def get_doc(self, db_name, doc_name, username, password):

        response = requests.get(self.urlutil.get_doc_url(db_name, username, doc_name),
                     auth=(username, password),
                     headers={"content-type": "application/json"},
                     data=json.dumps({"foo": "bar"}))

        return response