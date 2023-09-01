import pytest
from dotenv import load_dotenv
import os
import requests
from data.data import valid_emails, valid_passwords

load_dotenv()

HOST = os.getenv("HOST")
TEST_EMAIL = os.getenv("TEST_EMAIL")


def test_registration(database):
    response = requests.post(
        HOST + "/auth/register", data={"email": TEST_EMAIL, "password": "12345678"}
    )
    sql_query = f"SELECT code FROM email_verifications WHERE email = '{TEST_EMAIL}'"
    cursor = database.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchone()
    confirm_email = requests.post(
        HOST + "/auth/verify-email-registration",
        data={"email": TEST_EMAIL, "code": result, "referrer": ""},
    )

    assert confirm_email.status_code == 201


@pytest.mark.parametrize("email", valid_emails)
def test_valid_registration_with_valid_emails(email):
    response = requests.post(
        HOST + "/auth/register", data={"email": email, "password": "12345678"}
    )
    assert response.status_code == 201


@pytest.mark.parametrize("password", valid_passwords)
def test_valid_registration_with_valid_passwords(password):
    response = requests.post(
        HOST + "/auth/register", data={"email": TEST_EMAIL, "password": password}
    )
    assert response.status_code == 201
