import requests
import pytest
from data.getenv import HOST, TEST_PASSWORD, TEST_EMAIL_TWO
from data.data import valid_emails, invalid_emails, valid_passwords, invalid_passwords


@pytest.mark.parametrize("email", valid_emails)
def test_invalid_login_with_unregistred_emails(email):
    response = requests.post(
        HOST + "/auth/login", data={"email": email, "password": TEST_PASSWORD}
    )
    assert response.status_code == 403


@pytest.mark.parametrize("email", invalid_emails)
def test_invalid_login_with_invalid_emails(email):
    response = requests.post(
        HOST + "/auth/login", data={"email": email, "password": TEST_PASSWORD}
    )
    assert response.status_code == 400


@pytest.mark.parametrize("password", invalid_passwords)
def test_invalid_login_with_invalid_passwords(password):
    response = requests.post(
        HOST + "/auth/login", data={"email": TEST_EMAIL_TWO, "password": password}
    )
    assert response.status_code == 400
