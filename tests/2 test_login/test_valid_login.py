import requests
from data.getenv import HOST, TEST_VALID_LOGIN_EMAIL, TEST_PASSWORD
import allure


@allure.title("POST /auth/login")
def test_1_valid_login(database):
    requests.post(
        HOST + "/auth/register",
        data={"email": TEST_VALID_LOGIN_EMAIL, "password": TEST_PASSWORD},
    )
    sql_query = (
        f"SELECT code FROM email_verifications WHERE email = '{TEST_VALID_LOGIN_EMAIL}'"
    )
    cursor = database.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchone()
    requests.post(
        HOST + "/auth/verify-email-registration",
        data={"email": TEST_VALID_LOGIN_EMAIL, "code": result, "referrer": ""},
    )

    response = requests.post(
        HOST + "/auth/login",
        data={"email": TEST_VALID_LOGIN_EMAIL, "password": TEST_PASSWORD},
    )
    assert response.json()["access_token"]
    assert response.json()["refresh_token"]
