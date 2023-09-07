import pytest
from data.getenv import HOST
from data.data import (
    invalid_space_id,
    invalid_names,
    valid_names,
    background_ids,
    valid_ids,
    invalid_orders,
    valid_orders,
    valid_emails,
    invalid_emails,
)
import allure


@allure.title("GET /spaces")
def test_1_get_spaces(login_spaces):
    response = login_spaces.get(HOST + "/spaces")
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Ваше первое пространство"


@allure.title("PATCH /user/startTrial")
def test_2_start_trial(login_spaces):
    response = login_spaces.patch(HOST + "/user/startTrial")
    assert response.status_code == 200


@allure.title("DELETE /spaces/space_id")
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_3_delete_invalid_id_spaces(login_spaces, space_id):
    response = login_spaces.delete(HOST + f"/spaces/{space_id}")
    assert response.status_code == 400


@allure.title("DELETE /spaces/space_id")
def test_4_delete_space(login_spaces):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]["id"]
    response = login_spaces.delete(HOST + f"/spaces/{space_id}")
    get_spaces = login_spaces.get(HOST + "/spaces").json()
    assert response.status_code == 200
    assert len(get_spaces) == 0


@allure.title("POST /spaces")
def test_5_create_valid_space(login_spaces):
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
def test_6_create_invalid_space(login_spaces, name):
    create_space = login_spaces.post(HOST + "/spaces", data={"name": name})
    response = login_spaces.get(HOST + "/spaces").json()
    assert len(response) == 1
    assert create_space.status_code == 400


@pytest.mark.parametrize("space_id", invalid_space_id)
@pytest.mark.parametrize("name", valid_names)
@allure.title("PATCH /spaces/space_id/name")
def test_7_patch_name_invalid_space_id(login_spaces, space_id, name):
    create_space = login_spaces.patch(
        HOST + f"/spaces/{space_id}/name", data={"name": name}
    )
    assert create_space.status_code == 400


@pytest.mark.parametrize("name", valid_names)
@allure.title("PATCH /spaces/space_id/name")
def test_8_patch_name_valid_space_id(login_spaces, name):
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
def test_9_get_invalid_background_space(login_spaces, space_id):
    response = login_spaces.get(HOST + f"/spaces/{space_id}/background")
    assert response.status_code == 400


@allure.title("GET /spaces/space_id/background")
def test_10_get_valid_background_space(login_spaces):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]["id"]
    response = login_spaces.get(HOST + f"/spaces/{space_id}/background")
    assert response.status_code == 200


@allure.title("PATCH /spaces/space_id/background")
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_11_patch_invalid_background_space(login_spaces, space_id):
    response = login_spaces.patch(HOST + f"/spaces/{space_id}/background")
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/background")
@pytest.mark.parametrize("background_id", background_ids)
def test_12_patch_valid_background_space(login_spaces, background_id):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/background", json={"backgroundId": background_id}
    )
    assert response.json() == background_id


@allure.title("POST /spaces/join")
@pytest.mark.parametrize("token", invalid_space_id)
def test_13_join_to_invalid_space(login_spaces, token):
    response = login_spaces.post(HOST + f"/spaces/join", data={"token": token})
    assert response.status_code == 404


@allure.title("GET /spaces/joinData/token")
def test_14_get_space_data_from_token(login_spaces):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]
    space_token = space_id["shareLink"]["token"]
    response = login_spaces.get(HOST + f"/spaces/joinData/{space_token}")
    assert response.status_code == 200


@allure.title("GET /spaces/joinData/token")
@pytest.mark.parametrize("token", invalid_space_id)
def test_15_get_space_data_from_invalid_token(login_spaces, token):
    response = login_spaces.get(HOST + f"/spaces/joinData/{token}")
    assert response.status_code == 404


@allure.title("POST /spaces/space_id/share-link/off")
def test_17_space_share_link_off(login_spaces):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]["id"]
    response = login_spaces.post(HOST + f"/spaces/{space_id}/share-link/off")
    assert response.status_code == 201


@allure.title("POST /spaces/space_id/share-link/on")
def test_18_space_share_link_on(login_spaces):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]["id"]
    response = login_spaces.post(HOST + f"/spaces/{space_id}/share-link/on")
    assert response.status_code == 201


@allure.title("POST /spaces/space_id/share-link/off")
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_19_invalid_space_share_link_on(login_spaces, space_id):
    response = login_spaces.post(HOST + f"/spaces/{space_id}/share-link/off")
    assert response.status_code == 400


@allure.title("POST /spaces/space_id/share-link/on")
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_20_invalid_space_share_link_on(login_spaces, space_id):
    response = login_spaces.post(HOST + f"/spaces/{space_id}/share-link/on")
    assert response.status_code == 400


@allure.title("GET /spaces/space_id/projects")
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_21_get_projects_from_invalid_space(login_spaces, space_id):
    response = login_spaces.get(HOST + f"/spaces/{space_id}/projects")
    assert response.status_code == 400


@allure.title("GET /spaces/space_id/projects")
def test_22_get_projects_from_valid_space(login_spaces):
    space_id = login_spaces.get(HOST + "/spaces").json()[0]["id"]
    response = login_spaces.get(HOST + f"/spaces/{space_id}/projects")
    assert response.status_code == 200


@allure.title("DELETE /spaces/space_id/members/member_id")
def test_23_delete_member_from_space(login_spaces):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_member_id = space["members"][0]["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/members/{space_member_id}"
    )
    assert response.status_code == 200


@allure.title("DELETE /spaces/space_id/members/member_id")
@pytest.mark.parametrize("space_member_id", invalid_space_id)
def test_24_delete_invalid_members_from_space(login_spaces, space_member_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/members/{space_member_id}"
    )
    assert response.status_code == 400


@allure.title("DELETE /spaces/space_id/members/member_id")
@pytest.mark.parametrize("space_member_id", valid_ids)
def test_25_delete_invalid_members_from_space(login_spaces, space_member_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/members/{space_member_id}"
    )
    assert response.status_code == 404


@allure.title("PATCH /spaces/space_id/order")
@pytest.mark.parametrize("order", invalid_orders)
def test_26_change_invalid_order_space(login_spaces, order):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/order", json={"order": order}
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/order")
@pytest.mark.parametrize("order", valid_orders)
def test_27_change_order_space(login_spaces, order):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/order", json={"order": order}
    )
    assert response.status_code == 200


@allure.title("PATCH /spaces/space_id/order")
@pytest.mark.parametrize("order", valid_orders)
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_28_change_order_invalid_space(login_spaces, order, space_id):
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/order", json={"order": order}
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/columns/column_id")
@pytest.mark.parametrize("order", valid_orders)
def test_29_change_column_order_space(login_spaces, order):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_column_id = space["columns"][0]["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}", json={"order": order}
    )
    assert response.status_code == 200


@allure.title("PATCH /spaces/space_id/columns/column_id")
@pytest.mark.parametrize("order", invalid_orders)
def test_30_change_column_invalid_order_space(login_spaces, order):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_column_id = space["columns"][0]["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}", json={"order": order}
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/columns/column_id")
@pytest.mark.parametrize("order", valid_orders)
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_31_change_column_invalid_order_space(login_spaces, order, space_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}", json={"order": order}
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/columns/column_id")
@pytest.mark.parametrize("order", valid_orders)
@pytest.mark.parametrize("space_column_id", invalid_space_id)
def test_32_change_column_invalid_order_space(login_spaces, order, space_column_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}", json={"order": order}
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/columns/column_id")
@pytest.mark.parametrize("order", valid_orders)
@pytest.mark.parametrize("space_column_id", valid_ids)
def test_33_change_invalid_column_order_space(login_spaces, order, space_column_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}", json={"order": order}
    )
    assert response.status_code == 404


@allure.title("DELETE /spaces/space_id/columns/column_id")
@pytest.mark.parametrize("space_id", invalid_space_id)
@pytest.mark.parametrize("space_column_id", valid_ids)
def test_34_delete_column_with_invalid_space_id(
    login_spaces, space_column_id, space_id
):
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}"
    )
    assert response.status_code == 400


@allure.title("DELETE /spaces/space_id/columns/column_id")
@pytest.mark.parametrize("space_column_id", valid_ids)
def test_35_delete_invalid_column_with_space_id(login_spaces, space_column_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}"
    )
    assert response.status_code == 404


@allure.title("DELETE /spaces/space_id/columns/column_id")
@pytest.mark.parametrize("space_column_id", invalid_space_id)
def test_36_delete_invalid_column_with_space_id(login_spaces, space_column_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}"
    )
    assert response.status_code == 400


@allure.title("DELETE /spaces/space_id/columns/column_id")
def test_37_delete_column_with_space_id(login_spaces):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_column_id = space["columns"][0]["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}"
    )
    assert response.status_code == 200


@allure.title("POST /spaces/space_id/columns")
def test_38_create_column_into_space(login_spaces):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.post(
        HOST + f"/spaces/{space_id}/columns", json={"name": "Колонка", "order": 1}
    )
    assert response.status_code == 201


@allure.title("POST /spaces/space_id/columns")
@pytest.mark.parametrize("name", invalid_names)
def test_39_create_column_into_space(login_spaces, name):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.post(
        HOST + f"/spaces/{space_id}/columns", json={"name": name, "order": 1}
    )
    assert response.status_code == 400


@allure.title("POST /spaces/space_id/columns")
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_40_create_column_into_invalid_space(login_spaces, space_id):
    response = login_spaces.post(
        HOST + f"/spaces/{space_id}/columns", json={"name": "Колонка", "order": 2}
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/columns/column_id/name")
@pytest.mark.parametrize("space_id", invalid_space_id)
@pytest.mark.parametrize("space_column_id", invalid_space_id)
def test_41_change_column_name_with_invalid_space_and_invalid_column(
    login_spaces, space_id, space_column_id
):
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}/name",
        json={"name": "Колонка"},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/columns/column_id/name")
@pytest.mark.parametrize("space_column_id", invalid_space_id)
def test_42_change_column_name_with_invalid_column(login_spaces, space_column_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}/name",
        json={"name": "Колонка"},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/columns/column_id/name")
@pytest.mark.parametrize("space_column_id", valid_ids)
def test_43_change_column_name_with_invalid_column(login_spaces, space_column_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}/name",
        json={"name": "Колонка"},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/columns/column_id/name")
@pytest.mark.parametrize("space_column_id", valid_ids)
def test_44_change_column_name_with_invalid_column(login_spaces, space_column_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}/name",
        json={"name": "Колонка"},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/columns/column_id/name")
@pytest.mark.parametrize("name", invalid_names)
def test_45_change_column_space_name_with_invalid_name(login_spaces, name):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_column_id = space["columns"][0]["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}/name",
        json={"name": name},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/columns/column_id/name")
@pytest.mark.parametrize("name", valid_names)
def test_46_change_column_name_into_space(login_spaces, name):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_column_id = space["columns"][0]["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/columns/{space_column_id}/name",
        json={"name": name},
    )
    assert response.status_code == 200


@allure.title("POST /spaces/space_id/reglament-columns")
def test_47_create_reglament_column_into_space(login_spaces):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.post(
        HOST + f"/spaces/{space_id}/reglament-columns",
        json={"name": "Колонка", "order": 1},
    )
    assert response.status_code == 201


@allure.title("POST /spaces/space_id/reglament-columns")
@pytest.mark.parametrize("name", invalid_names)
def test_48_create_reglament_column_into_space(login_spaces, name):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.post(
        HOST + f"/spaces/{space_id}/reglament-columns", json={"name": name, "order": 1}
    )
    assert response.status_code == 400


@allure.title("POST /spaces/space_id/reglament-columns")
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_49_create_reglament_column_into_invalid_space(login_spaces, space_id):
    response = login_spaces.post(
        HOST + f"/spaces/{space_id}/reglament-columns",
        json={"name": "Колонка", "order": 2},
    )
    assert response.status_code == 400


@allure.title("GET /spaces/space_id/reglaments")
def test_50_get_space_reglaments(login_spaces):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.get(HOST + f"/spaces/{space_id}/reglaments")
    assert response.status_code == 200


@allure.title("GET /spaces/space_id/reglaments")
@pytest.mark.parametrize("space_id", invalid_space_id)
def test_51_get_invalid_space_reglaments(login_spaces, space_id):
    response = login_spaces.get(HOST + f"/spaces/{space_id}/reglaments")
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/name")
@pytest.mark.parametrize("space_id", invalid_space_id)
@pytest.mark.parametrize("space_reglament_column_id", invalid_space_id)
def test_52_change_reglament_column_name_with_invalid_space_and_invalid_column(
    login_spaces, space_id, space_reglament_column_id
):
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/name",
        json={"name": "Колонка"},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/name")
@pytest.mark.parametrize("space_reglament_column_id", invalid_space_id)
def test_53_change_reglament_column_name_with_invalid_column(
    login_spaces, space_reglament_column_id
):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/name",
        json={"name": "Колонка"},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/name")
@pytest.mark.parametrize("space_reglament_column_id", valid_ids)
def test_54_change_reglament_column_name_with_invalid_column(
    login_spaces, space_reglament_column_id
):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/name",
        json={"name": "Колонка"},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/name")
@pytest.mark.parametrize("space_reglament_column_id", valid_ids)
def test_55_change_reglament_column_name_with_invalid_column(
    login_spaces, space_reglament_column_id
):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/name",
        json={"name": "Колонка"},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/name")
@pytest.mark.parametrize("name", invalid_names)
def test_56_change_reglament_column_space_name_with_invalid_name(login_spaces, name):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/name",
        json={"name": name},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/name")
@pytest.mark.parametrize("name", valid_names)
def test_57_change_reglament_column_name_into_space(login_spaces, name):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_spaces.patch(
        HOST + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/name",
        json={"name": name},
    )
    assert response.status_code == 200


@allure.title("DELETE /spaces/space_id/reglament-columns/column_id")
@pytest.mark.parametrize("space_id", invalid_space_id)
@pytest.mark.parametrize("space_reglament_column_id", valid_ids)
def test_58_delete_reglament_column_with_invalid_space_id(
    login_spaces, space_reglament_column_id, space_id
):
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/columns/{space_reglament_column_id}"
    )
    assert response.status_code == 400


@allure.title("DELETE /spaces/space_id/reglament-columns/column_id")
@pytest.mark.parametrize("space_reglament_column_id", valid_ids)
def test_59_delete_invalid_reglament_column_with_space_id(
    login_spaces, space_reglament_column_id
):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/columns/{space_reglament_column_id}"
    )
    assert response.status_code == 404


@allure.title("DELETE /spaces/space_id/reglament-columns/column_id")
@pytest.mark.parametrize("space_reglament_column_id", invalid_space_id)
def test_60_delete_invalid_reglament_column_with_space_id(
    login_spaces, space_reglament_column_id
):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/columns/{space_reglament_column_id}"
    )
    assert response.status_code == 400


@allure.title("DELETE /spaces/space_id/reglament-columns/column_id")
def test_61_delete_reglament_column_with_space_id(login_spaces):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_reglament_column_id = space["columns"][0]["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/columns/{space_reglament_column_id}"
    )
    assert response.status_code == 200


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/order")
@pytest.mark.parametrize("space_id", invalid_space_id)
@pytest.mark.parametrize("space_reglament_column_id", invalid_space_id)
@pytest.mark.parametrize("order", invalid_orders)
def test_62_change_reglament_column_order_with_invalid_space_and_invalid_column(
    login_spaces, space_id, space_reglament_column_id, order
):
    response = login_spaces.patch(
        HOST
        + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/order",
        json={"order": order},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/order")
@pytest.mark.parametrize("space_reglament_column_id", invalid_space_id)
@pytest.mark.parametrize("order", invalid_orders)
def test_63_change_reglament_column_order_with_invalid_column(
    login_spaces, space_reglament_column_id, order
):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST
        + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/order",
        json={"order": order},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/order")
@pytest.mark.parametrize("space_reglament_column_id", valid_ids)
@pytest.mark.parametrize("order", invalid_orders)
def test_64_change_reglament_column_order_with_invalid_column(
    login_spaces, space_reglament_column_id, order
):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST
        + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/order",
        json={"order": order},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/order")
@pytest.mark.parametrize("space_reglament_column_id", valid_ids)
@pytest.mark.parametrize("order", invalid_orders)
def test_65_change_reglament_column_order_with_invalid_column(
    login_spaces, space_reglament_column_id, order
):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.patch(
        HOST
        + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/order",
        json={"order": order},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/order")
@pytest.mark.parametrize("order", invalid_orders)
def test_66_change_reglament_column_space_name_with_invalid_name(login_spaces, order):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_spaces.patch(
        HOST
        + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/order",
        json={"order": order},
    )
    assert response.status_code == 400


@allure.title("PATCH /spaces/space_id/reglaments-columns/column_id/order")
@pytest.mark.parametrize("order", valid_orders)
def test_67_change_reglament_column_order_into_space(login_spaces, order):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_spaces.patch(
        HOST
        + f"/spaces/{space_id}/reglament-columns/{space_reglament_column_id}/order",
        json={"order": order},
    )
    assert response.status_code == 200


@pytest.mark.parametrize("email", valid_emails)
@allure.title("POST /spaces/space_id/share")
def test_68_share_valid_email_to_space(login_spaces, email):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.post(
        HOST + f"/spaces/{space_id}/share", json={"email": email}
    )
    assert response.status_code == 201


@pytest.mark.parametrize("email", invalid_emails)
@allure.title("POST /spaces/space_id/share")
def test_69_share_invalid_email_to_space(login_spaces, email):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.post(
        HOST + f"/spaces/{space_id}/share", json={"email": email}
    )
    assert response.status_code == 400


@allure.title("DELETE /spaces/space_id/invite/remove")
def test_70_remove_invite_to_space(login_spaces):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_member_invite_id = space["invites"][0]["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/invite/remove", json={"id": space_member_invite_id}
    )
    assert response.status_code == 200


@allure.title("DELETE /spaces/space_id/invite/remove")
@pytest.mark.parametrize("space_member_invite_id", invalid_space_id)
def test_71_remove_invalid_invite_to_space(login_spaces, space_member_invite_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/invite/remove", json={"id": space_member_invite_id}
    )
    assert response.status_code == 400


@allure.title("DELETE /spaces/space_id/invite/remove")
@pytest.mark.parametrize("space_member_invite_id", invalid_orders)
def test_72_remove_invalid_invite_to_space(login_spaces, space_member_invite_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/invite/remove", json={"id": space_member_invite_id}
    )
    assert response.status_code == 400


@allure.title("DELETE /spaces/space_id/invite/remove")
def test_73_remove_invalid_invite_to_space(login_spaces):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    space_member_invite_id = space["invites"][0]["id"] + 777
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/invite/remove", json={"id": space_member_invite_id}
    )
    assert response.status_code == 400


@allure.title("DELETE /spaces/space_id/invite/remove")
@pytest.mark.parametrize("space_member_invite_id", valid_orders)
def test_74_remove_invalid_invite_to_space(login_spaces, space_member_invite_id):
    space = login_spaces.get(HOST + "/spaces").json()[0]
    space_id = space["id"]
    response = login_spaces.delete(
        HOST + f"/spaces/{space_id}/invite/remove", json={"id": space_member_invite_id}
    )
    assert response.status_code == 400
