import pytest
import psycopg2
from data.getenv import DB, DB_HOST, DB_PORT, DB_PASSWORD, DB_USERNAME


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
