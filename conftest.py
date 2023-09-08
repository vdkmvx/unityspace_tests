import pytest
import psycopg2
import requests
from data.getenv import (
    DB,
    DB_HOST,
    DB_PORT,
    DB_PASSWORD,
    DB_USERNAME,
    HOST,
    TEST_PASSWORD,
    TEST_EMAIL_SPACES,
    TEST_EMAIL_PROJECTS,
)


@pytest.fixture(scope="session")
def database():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB,
            user=DB_USERNAME,
            password=DB_PASSWORD,
        )
        yield connection
        connection.close()
    except:
        print("Can`t establish connection to database")


@pytest.fixture(scope="session")
def login_spaces(database):
    requests.post(
        HOST + "/auth/register",
        data={"email": TEST_EMAIL_SPACES, "password": TEST_PASSWORD},
    )
    sql_query = (
        f"SELECT code FROM email_verifications WHERE email = '{TEST_EMAIL_SPACES}'"
    )
    cursor = database.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchone()
    requests.post(
        HOST + "/auth/verify-email-registration",
        data={"email": TEST_EMAIL_SPACES, "code": result, "referrer": ""},
    )

    _session = requests.Session()
    response = requests.post(
        HOST + "/auth/login",
        data={"email": TEST_EMAIL_SPACES, "password": TEST_PASSWORD},
    )
    auth = response.json()["access_token"]
    _session.headers.update({"Authorization": f"Bearer {auth}"})
    yield _session
    try:
        sql_drop_table = 'DELETE FROM users WHERE "id" >= 1;'
        cursor.execute(sql_drop_table)
        database.commit()  # Commit the changes to the database
    except Exception as e:
        database.rollback()  # Rollback changes in case of an exception
        print(f"Error during cleanup: {str(e)}")


@pytest.fixture(scope="session")
def login_projects(database):
    requests.post(
        HOST + "/auth/register",
        data={"email": TEST_EMAIL_PROJECTS, "password": TEST_PASSWORD},
    )
    sql_query = (
        f"SELECT code FROM email_verifications WHERE email = '{TEST_EMAIL_PROJECTS}'"
    )
    cursor = database.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchone()
    requests.post(
        HOST + "/auth/verify-email-registration",
        data={"email": TEST_EMAIL_PROJECTS, "code": result, "referrer": ""},
    )

    _session = requests.Session()
    response = requests.post(
        HOST + "/auth/login",
        data={"email": TEST_EMAIL_PROJECTS, "password": TEST_PASSWORD},
    )
    auth = response.json()["access_token"]
    _session.headers.update({"Authorization": f"Bearer {auth}"})
    # return _session
    yield _session
    try:
        sql_drop_table = 'DELETE FROM users WHERE "id" >= 1;'
        cursor.execute(sql_drop_table)
        database.commit()  # Commit the changes to the database
    except Exception as e:
        database.rollback()  # Rollback changes in case of an exception
        print(f"Error during cleanup: {str(e)}")
