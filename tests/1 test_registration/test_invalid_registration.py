from data.data import invalid_emails, invalid_passwords, valid_emails
from data.getenv import HOST, TEST_PASSWORD
import requests
import pytest
import allure


@allure.title("POST /auth/register")
@pytest.mark.parametrize("email", invalid_emails)
def test_1_invalid_registration_with_invalid_emails(email):
    response = requests.post(
        HOST + "/auth/register", data={"email": email, "password": TEST_PASSWORD}
    )
    assert response.status_code == 400


@allure.title("POST /auth/register")
@pytest.mark.parametrize("email", valid_emails)
@pytest.mark.parametrize("password", invalid_passwords)
def test_2_invalid_registration_with_invalid_passwords(password, email):
    response = requests.post(
        HOST + "/auth/register",
        data={"email": email, "password": password},
    )
    assert response.status_code == 400
