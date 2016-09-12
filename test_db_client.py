"""
Class that automates testing of creating a database and a database document.

run with

nosetests -v --nocapture test/test_db_client.py

or

nosetests -v test/test_db_client.py

"""

import ConfigParser

from db_client import db_client


class test_db_client:
    """
        This class tests the ImageCommand
    """

    Config = ConfigParser.ConfigParser()
    client = db_client()

    def __init__(self):
        self.Config.read("test_config.ini")


    def test_create_db(self):
        """
        Test to create db.
        """

        db_name = self.Config.get("Configuration", "db_name")
        username = self.Config.get("Credentials", "username")
        password = self.Config.get("Credentials", "password")

        response = self.client.create_new_database(db_name, username, password)

        assert response.status_code == 201


    def test_create_doc(self):
        """
        Test to create document.
        """

        db_name = self.Config.get("Configuration", "db_name")
        doc_name = self.Config.get("Configuration", "db_doc_name")
        username = self.Config.get("Credentials", "username")
        password = self.Config.get("Credentials", "password")

        response = self.client.create_new_doc(db_name, doc_name, username, password)

        assert response.status_code == 201


    def test_validate_doc(self):
        """
        Test to validate document.
        """

        db_name = self.Config.get("Configuration", "db_name")
        doc_name = self.Config.get("Configuration", "db_doc_name")
        username = self.Config.get("Credentials", "username")
        password = self.Config.get("Credentials", "password")

        response = self.client.get_doc(db_name, doc_name, username, password)

        assert response.status_code == 200