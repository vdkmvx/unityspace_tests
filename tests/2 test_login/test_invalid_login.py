import requests
import pytest
import allure
from data.getenv import HOST, TEST_PASSWORD, TEST_INVALID_LOGIN_EMAIL
from data.data import valid_emails, invalid_emails, invalid_passwords


@pytest.mark.parametrize("email", valid_emails)
def test_1_invalid_login_with_unregistred_emails(email):
    response = requests.post(
        HOST + "/auth/login", data={"email": email, "password": TEST_PASSWORD}
    )
    assert response.status_code == 403


@pytest.mark.parametrize("email", invalid_emails)
def test_2_invalid_login_with_invalid_emails(email):
    response = requests.post(
        HOST + "/auth/login", data={"email": email, "password": TEST_PASSWORD}
    )
    assert response.status_code == 400


@allure.title("POST /auth/login")
@pytest.mark.parametrize("password", invalid_passwords)
def test_3_invalid_login_with_invalid_passwords(password):
    response = requests.post(
        HOST + "/auth/login",
        data={"email": TEST_INVALID_LOGIN_EMAIL, "password": password},
    )
    assert response.status_code == 400
