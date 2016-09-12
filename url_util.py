
class url_util:

    def get_database_url(self, db_name, username):
        return "https://{0}.cloudant.com/{1}".format(username, db_name)

    def get_db_create_url(self, db_name, username):
        return "https://{0}.cloudant.com/{1}".format(username, db_name)

    def get_doc_create_url(self, db_name, username, doc_name):
        return "https://{0}.cloudant.com/{1}/{2}".format(username, db_name, doc_name)

    def get_doc_url(self, db_name, username, doc_name):
        return "https://{0}.cloudant.com/{1}/{2}".format(username, db_name, doc_name)