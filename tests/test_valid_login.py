import requests
from data.getenv import HOST, TEST_EMAIL, TEST_PASSWORD


def test_login():
    response = requests.post(
        HOST + "/auth/login", data={"email": TEST_EMAIL, "password": TEST_PASSWORD}
    )
    assert response.json()["access_token"]
    assert response.json()["refresh_token"]
