from data.data import invalid_emails, invalid_passwords
from data.getenv import HOST, TEST_PASSWORD
import requests
import pytest


@pytest.mark.parametrize("email", invalid_emails)
def test_invalid_registration_with_invalid_emails(email):
    response = requests.post(
        HOST + "/auth/register", data={"email": email, "password": TEST_PASSWORD}
    )
    assert response.status_code == 400


@pytest.mark.parametrize("password", invalid_passwords)
def test_invalid_registration_with_invalid_passwords(password):
    response = requests.post(
        HOST + "/auth/register",
        data={"email": "password@test.ru", "password": password},
    )
    assert response.status_code == 400
