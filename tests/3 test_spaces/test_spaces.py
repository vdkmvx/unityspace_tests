import pytest
from data.getenv import HOST
from data.data import invalid_space_id
import allure


@allure.title("GET /spaces")
def test_get_spaces(login_spaces):
    response = login_spaces.get(HOST + "/spaces")
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Ваше первое пространство"


@allure.title("PATCH /user/startTrial")
def test_start_trial(login_spaces):
    response = login_spaces.patch(HOST + "/user/startTrial")
    assert response.status_code == 200


@allure.title("DELETE /spaces/space_id")
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_delete_invalid_id_spaces(login_spaces, space_id):
    response = login_spaces.delete(HOST + f"/spaces/{space_id}")
    assert response.status_code == 400


@allure.title("DELETE /spaces/space_id")
def test_delete_space(login_spaces):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]["id"]
    response = login_spaces.delete(HOST + f"/spaces/{space_id}")
    get_spaces = login_spaces.get(HOST + "/spaces").json()
    assert response.status_code == 200
    assert len(get_spaces) == 0
