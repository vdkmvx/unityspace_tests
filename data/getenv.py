from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
TEST_VALID_REGISTRATION_EMAIL = os.getenv("TEST_VALID_REGISTRATION_EMAIL")
TEST_VALID_REGISTRATION_EMAIL_TWO = os.getenv("TEST_VALID_REGISTRATION_EMAIL_TWO")
TEST_USER_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")
TEST_VALID_LOGIN_EMAIL = os.getenv("TEST_VALID_LOGIN_EMAIL")
TEST_INVALID_LOGIN_EMAIL = os.getenv("TEST_INVALID_LOGIN_EMAIL")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB = os.getenv("DB")
TEST_EMAIL_SPACES = os.getenv("TEST_EMAIL_SPACES")
TEST_EMAIL_PROJECTS = os.getenv("TEST_EMAIL_PROJECTS")
TEST_EMAIL_TASKS = os.getenv("TEST_EMAIL_TASKS")
TEST_EMAIL_REGLAMENTS = os.getenv("TEST_EMAIL_REGLAMENTS")
