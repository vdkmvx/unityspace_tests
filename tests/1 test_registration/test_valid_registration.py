import pytest
import requests
from data.data import valid_emails, valid_passwords
from data.getenv import TEST_EMAIL_TWO, TEST_EMAIL, HOST, TEST_PASSWORD


def test_registration(database):
    requests.post(
        HOST + "/auth/register", data={"email": TEST_EMAIL, "password": TEST_PASSWORD}
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
        HOST + "/auth/register", data={"email": email, "password": TEST_PASSWORD}
    )
    assert response.status_code == 201


@pytest.mark.parametrize("password", valid_passwords)
def test_valid_registration_with_valid_passwords(password):
    response = requests.post(
        HOST + "/auth/register", data={"email": TEST_EMAIL_TWO, "password": password}
    )
    assert response.status_code == 201
