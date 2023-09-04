import pytest
from data.getenv import HOST
from data.data import invalid_space_id, invalid_names, valid_names
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


@allure.title("POST /spaces")
def test_create_valid_space(login_spaces):
    create_space = login_spaces.post(
        HOST + "/spaces", data={"name": "Тестовое пространство"}
    )
    space_id = create_space.json()["id"]
    response = login_spaces.get(HOST + "/spaces").json()
    assert create_space.status_code == 201
    assert response[0]["id"] == space_id
    assert len(response) == 1


@pytest.mark.parametrize("name", invalid_names)
@allure.title("POST /spaces")
def test_create_invalid_space(login_spaces, name):
    create_space = login_spaces.post(HOST + "/spaces", data={"name": name})
    response = login_spaces.get(HOST + "/spaces").json()
    assert len(response) == 1
    assert create_space.status_code == 400


@pytest.mark.parametrize("space_id", invalid_space_id)
@pytest.mark.parametrize("name", valid_names)
@allure.title("PATCH /spaces/space_id/name")
def test_patch_name_invalid_space_id(login_spaces, space_id, name):
    create_space = login_spaces.patch(
        HOST + f"/spaces/{space_id}/name", data={"name": name}
    )
    assert create_space.status_code == 400


@pytest.mark.parametrize("name", valid_names)
@allure.title("PATCH /spaces/space_id/name")
def test_patch_name_valid_space_id(login_spaces, name):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    create_space = login_spaces.patch(
        HOST + f"/spaces/{space_id}/name", data={"name": name}
    )
    space_name = create_space.json()["name"]
    assert create_space.status_code == 200
    assert space_name == create_space.json()["name"]
