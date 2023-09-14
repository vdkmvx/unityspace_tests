from data.getenv import HOST
from data.data import (
    valid_ids,
    invalid_space_id,
    valid_names,
    invalid_names,
    invalid_orders,
    valid_orders,
)
import allure
import pytest


@allure.title("GET /reglaments")
def test_1_get_reglaments(login_reglaments):
    response = login_reglaments.get(HOST + "/reglaments")
    assert response.status_code == 200


@allure.title("POST /reglaments")
def test_2_create_reglament(login_reglaments):
    space = login_reglaments.get(HOST + "/spaces").json()[0]
    reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_reglaments.post(
        HOST + "/reglaments",
        json={
            "name": "string",
            "reglamentColumnId": reglament_column_id,
            "content": "string",
            "order": 0,
        },
    )
    assert response.status_code == 201


@allure.title("POST /reglaments")
@pytest.mark.parametrize("reglament_column_id", invalid_space_id)
def test_3_create_reglament(login_reglaments, reglament_column_id):
    response = login_reglaments.post(
        HOST + "/reglaments",
        json={
            "name": "string",
            "reglamentColumnId": reglament_column_id,
            "content": "string",
            "order": 0,
        },
    )
    assert response.status_code == 400


@allure.title("POST /reglaments")
@pytest.mark.parametrize("reglament_column_id", valid_ids)
def test_4_create_reglament(login_reglaments, reglament_column_id):
    response = login_reglaments.post(
        HOST + "/reglaments",
        json={
            "name": "string",
            "reglamentColumnId": reglament_column_id,
            "content": "string",
            "order": 0,
        },
    )
    assert response.status_code == 400


@allure.title("POST /reglaments")
@pytest.mark.parametrize("name", valid_names)
def test_5_create_reglament(login_reglaments, name):
    space = login_reglaments.get(HOST + "/spaces").json()[0]
    reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_reglaments.post(
        HOST + "/reglaments",
        json={
            "name": name,
            "reglamentColumnId": reglament_column_id,
            "content": "string",
            "order": 0,
        },
    )
    assert response.status_code == 201


@allure.title("POST /reglaments")
@pytest.mark.parametrize("name", invalid_names)
def test_6_create_reglament(login_reglaments, name):
    space = login_reglaments.get(HOST + "/spaces").json()[0]
    reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_reglaments.post(
        HOST + "/reglaments",
        json={
            "name": name,
            "reglamentColumnId": reglament_column_id,
            "content": "string",
            "order": 0,
        },
    )
    assert response.status_code == 400


@allure.title("POST /reglaments")
@pytest.mark.parametrize("order", invalid_orders)
def test_7_create_reglament(login_reglaments, order):
    space = login_reglaments.get(HOST + "/spaces").json()[0]
    reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_reglaments.post(
        HOST + "/reglaments",
        json={
            "name": "string",
            "reglamentColumnId": reglament_column_id,
            "content": "string",
            "order": order,
        },
    )
    assert response.status_code == 400


@allure.title("POST /reglaments")
@pytest.mark.parametrize("order", valid_orders)
def test_8_create_reglament(login_reglaments, order):
    space = login_reglaments.get(HOST + "/spaces").json()[0]
    reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_reglaments.post(
        HOST + "/reglaments",
        json={
            "name": "string",
            "reglamentColumnId": reglament_column_id,
            "content": "string",
            "order": order,
        },
    )
    assert response.status_code == 201


@allure.title("PATCH /reglaments/reglament_id/required")
def test_9_change_reglament_to_required(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/required", json={"required": True}
    )
    assert response.status_code == 200


@allure.title("PATCH /reglaments/reglament_id/required")
def test_10_change_reglament_to_required(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/required", json={"required": False}
    )
    assert response.status_code == 200


@allure.title("PATCH /reglaments/reglament_id/required")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_11_change_reglament_to_required(login_reglaments, reglament_id):
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/required", json={"required": False}
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/required")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_12_change_reglament_to_required(login_reglaments, reglament_id):
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/required", json={"required": False}
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/intro")
def test_13_change_reglament_to_intro(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/intro", json={"intro": True}
    )
    assert response.status_code == 200


@allure.title("PATCH /reglaments/reglament_id/intro")
def test_14_change_reglament_to_intro(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/intro", json={"intro": False}
    )
    assert response.status_code == 200


@allure.title("PATCH /reglaments/reglament_id/intro")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_15_change_reglament_to_intro(login_reglaments, reglament_id):
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/intro", json={"intro": False}
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/intro")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_16_change_reglament_to_intro(login_reglaments, reglament_id):
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/intro", json={"intro": False}
    )
    assert response.status_code == 400


@allure.title("GET /reglaments/reglament_id")
def test_17_get_full_reglament(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.get(HOST + f"/reglaments/{reglament_id}")
    assert response.status_code == 200


@allure.title("GET /reglaments/reglament_id")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_18_get_full_reglament(login_reglaments, reglament_id):
    response = login_reglaments.get(HOST + f"/reglaments/{reglament_id}")
    assert response.status_code == 400


@allure.title("GET /reglaments/reglament_id")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_19_get_full_reglament(login_reglaments, reglament_id):
    response = login_reglaments.get(HOST + f"/reglaments/{reglament_id}")
    assert response.status_code == 400


@allure.title("DELETE /reglaments/reglament_id")
def test_20_delete_reglament(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.delete(HOST + f"/reglaments/{reglament_id}")
    assert response.status_code == 200


@allure.title("DELETE /reglaments/reglament_id")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_21_delete_reglament(login_reglaments, reglament_id):
    response = login_reglaments.delete(HOST + f"/reglaments/{reglament_id}")
    assert response.status_code == 400


@allure.title("DELETE /reglaments/reglament_id")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_22_delete_reglament(login_reglaments, reglament_id):
    response = login_reglaments.delete(HOST + f"/reglaments/{reglament_id}")
    assert response.status_code == 400


@allure.title("DELETE /reglaments/reglament_id/usersPassed")
def test_23_delete_users_passed_reglament(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.delete(HOST + f"/reglaments/{reglament_id}/usersPassed")
    assert response.status_code == 200


@allure.title("DELETE /reglaments/reglament_id/usersPassed")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_24_delete_users_passed_reglament(login_reglaments, reglament_id):
    response = login_reglaments.delete(HOST + f"/reglaments/{reglament_id}/usersPassed")
    assert response.status_code == 400


@allure.title("DELETE /reglaments/reglament_id/usersPassed")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_25_delete_users_passed_reglament(login_reglaments, reglament_id):
    response = login_reglaments.delete(HOST + f"/reglaments/{reglament_id}/usersPassed")
    assert response.status_code == 400


@allure.title("GET /reglaments/reglament_id/questions")
def test_26_get_questions_reglament(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.get(HOST + f"/reglaments/{reglament_id}/questions")
    assert response.status_code == 200


@allure.title("GET /reglaments/reglament_id/questions")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_27_get_questions_reglament(login_reglaments, reglament_id):
    response = login_reglaments.get(HOST + f"/reglaments/{reglament_id}/questions")
    assert response.status_code == 400


@allure.title("GET /reglaments/reglament_id/questions")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_28_get_questions_reglament(login_reglaments, reglament_id):
    response = login_reglaments.get(HOST + f"/reglaments/{reglament_id}/questions")
    assert response.status_code == 400
