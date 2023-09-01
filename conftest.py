from dotenv import load_dotenv
import pytest
import os
import psycopg2

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB = os.getenv('DB')


@pytest.fixture()
def database():
    try:
        connection = psycopg2.connect(host=DB_HOST,
                                      port=DB_PORT,
                                      database=DB,
                                      user=DB_USERNAME,
                                      password=DB_PASSWORD
                                      )
        yield connection
        connection.close()
    except:
        print('Can`t establish connection to database')
