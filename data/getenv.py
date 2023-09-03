from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_EMAIL_TWO = os.getenv("TEST_EMAIL_TWO")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB = os.getenv("DB")
