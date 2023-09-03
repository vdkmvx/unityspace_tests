import pytest
from data.getenv import HOST


def test_get_spaces(login_spaces):
    response = login_spaces.get(HOST + "/spaces")
    print(response.json())
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Ваше первое пространство"


def test_start_trial(login_spaces):
    response = login_spaces.patch(HOST + "/user/startTrial")
    assert response.status_code == 200
