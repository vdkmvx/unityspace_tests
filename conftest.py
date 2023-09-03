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
    TEST_EMAIL,
)


@pytest.fixture()
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
def login():
    _session = requests.Session()
    print(_session.headers)
    response = requests.post(
        HOST + "/auth/login", data={"email": TEST_EMAIL, "password": TEST_PASSWORD}
    )
    auth = response.json()["access_token"]
    _session.headers.update({"Authorization": f"Bearer {auth}"})
    return _session
