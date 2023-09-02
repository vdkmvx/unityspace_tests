from data.data import invalid_emails, invalid_passwords, valid_emails
import requests
from dotenv import load_dotenv
import os
import pytest

load_dotenv()

HOST = os.getenv("HOST")


@pytest.mark.parametrize("email", invalid_emails)
def test_invalid_registration_with_invalid_emails(email):
    response = requests.post(
        HOST + "/auth/register", data={"email": email, "password": "12345678"}
    )
    assert response.status_code == 400


@pytest.mark.parametrize("password", invalid_passwords)
def test_invalid_registration_with_invalid_passwords(password):
    response = requests.post(
        HOST + "/auth/register",
        data={"email": "password@test.ru", "password": password},
    )
    assert response.status_code == 400
