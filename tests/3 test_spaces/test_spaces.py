import pytest
from data.getenv import HOST
from data.data import invalid_space_id, invalid_names, valid_names, background_ids
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


@allure.title("GET /spaces/space_id/background")
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_get_invalid_background_space(login_spaces, space_id):
    response = login_spaces.get(HOST + f"/spaces/{space_id}/background")
    assert response.status_code == 400


@allure.title("GET /spaces/space_id/background")
def test_get_valid_background_space(login_spaces):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]["id"]
    response = login_spaces.get(HOST + f"/spaces/{space_id}/background")
    assert response.status_code == 200


@allure.title("PATCH /spaces/space_id/background")
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_patch_invalid_background_space(login_spaces, space_id):
    response = login_spaces.patch(HOST + f"/spaces/{space_id}/background")
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/background")
@pytest.mark.parametrize("background_id", background_ids)
def test_patch_valid_background_space(login_spaces, background_id):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/background", json={"backgroundId": background_id}
    )
    assert response.json() == background_id


@allure.title("POST /spaces/join")
@pytest.mark.parametrize("token", invalid_space_id)
def test_join_to_invalid_space(login_spaces, token):
    response = login_spaces.post(HOST + f"/spaces/join", data={"token": token})
    assert response.status_code == 404


@allure.title("GET /spaces/joinData/token")
def test_get_space_data_from_token(login_spaces):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]
    space_token = space_id["shareLink"]["token"]
    response = login_spaces.get(HOST + f"/spaces/joinData/{space_token}")
    assert response.status_code == 200


@allure.title("GET /spaces/joinData/token")
@pytest.mark.parametrize("token", invalid_space_id)
def test_get_space_data_from_invalid_token(login_spaces, token):
    response = login_spaces.get(HOST + f"/spaces/joinData/{token}")
    assert response.status_code == 404


@allure.title("POST /spaces/space_id/share-link/off")
def test_space_share_link_off(login_spaces):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]["id"]
    response = login_spaces.post(HOST + f"/spaces/{space_id}/share-link/off")
    assert response.status_code == 201


@allure.title("POST /spaces/space_id/share-link/on")
def test_space_share_link_on(login_spaces):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]["id"]
    response = login_spaces.post(HOST + f"/spaces/{space_id}/share-link/on")
    assert response.status_code == 201
