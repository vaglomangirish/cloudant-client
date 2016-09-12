# cloudant-client
Repository contain code for simple client application for IBM Cloudant DB.

### Tools Used
- Python 2.7.11
- Nosetests framework.

### Steps to Run

- Clone the repository onto your local machine.
- Change your current working directory to the project directory.
- Install python prerequisite packages using #pip install -r requirements.txt.
- Replace db_name, db_doc_name, username and password in test_config.ini file.
- Execute the test suite by executing #nosetests -v test_db_client.py
- You should see the nosetests suite running automated tests for DB creation, Document creation and Document validation.