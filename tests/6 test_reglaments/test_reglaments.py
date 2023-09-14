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


@allure.title("POST /reglaments/reglament_id/questions")
@pytest.mark.parametrize("name", valid_names)
def test_29_create_questions_reglament(login_reglaments, name):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.post(
        HOST + f"/reglaments/{reglament_id}/questions", json={"name": name}
    )
    assert response.status_code == 201


@allure.title("POST /reglaments/reglament_id/questions")
@pytest.mark.parametrize("name", invalid_names)
def test_30_create_questions_reglament(login_reglaments, name):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.post(
        HOST + f"/reglaments/{reglament_id}/questions", json={"name": name}
    )
    assert response.status_code == 400


@allure.title("POST /reglaments/reglament_id/questions")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_31_create_questions_reglament(login_reglaments, reglament_id):
    response = login_reglaments.post(
        HOST + f"/reglaments/{reglament_id}/questions", json={"name": "string"}
    )
    assert response.status_code == 400


@allure.title("POST /reglaments/reglament_id/questions")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_32_create_questions_reglament(login_reglaments, reglament_id):
    response = login_reglaments.post(
        HOST + f"/reglaments/{reglament_id}/questions", json={"name": "string"}
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/changeReglamentColumnAndOrder")
def test_33_change_reglament_column_and_order(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    space = login_reglaments.get(HOST + "/spaces").json()[0]
    reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/changeReglamentColumnAndOrder",
        json={"columnId": reglament_column_id, "order": 0},
    )
    assert response.status_code == 200


@allure.title("PATCH /reglaments/reglament_id/changeReglamentColumnAndOrder")
@pytest.mark.parametrize("reglament_column_id", invalid_space_id)
def test_34_change_reglament_column_and_order(login_reglaments, reglament_column_id):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/changeReglamentColumnAndOrder",
        json={"columnId": reglament_column_id, "order": 0},
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/changeReglamentColumnAndOrder")
@pytest.mark.parametrize("reglament_column_id", valid_ids)
def test_35_change_reglament_column_and_order(login_reglaments, reglament_column_id):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/changeReglamentColumnAndOrder",
        json={"columnId": reglament_column_id, "order": 0},
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/changeReglamentColumnAndOrder")
@pytest.mark.parametrize("order", invalid_orders)
def test_36_change_reglament_column_and_order(login_reglaments, order):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    space = login_reglaments.get(HOST + "/spaces").json()[0]
    reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/changeReglamentColumnAndOrder",
        json={"columnId": reglament_column_id, "order": order},
    )
    assert response.status_code == 200


@allure.title("PATCH /reglaments/reglament_id/changeReglamentColumnAndOrder")
@pytest.mark.parametrize("order", valid_orders)
def test_37_change_reglament_column_and_order(login_reglaments, order):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    space = login_reglaments.get(HOST + "/spaces").json()[0]
    reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/changeReglamentColumnAndOrder",
        json={"columnId": reglament_column_id, "order": order},
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/changeReglamentColumnAndOrder")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_38_change_reglament_column_and_order(login_reglaments, reglament_id):
    space = login_reglaments.get(HOST + "/spaces").json()[0]
    reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/changeReglamentColumnAndOrder",
        json={"columnId": reglament_column_id, "order": 0},
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/changeReglamentColumnAndOrder")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_39_change_reglament_column_and_order(login_reglaments, reglament_id):
    space = login_reglaments.get(HOST + "/spaces").json()[0]
    reglament_column_id = space["reglamentColumns"][0]["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/changeReglamentColumnAndOrder",
        json={"columnId": reglament_column_id, "order": 0},
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/name")
@pytest.mark.parametrize("name", valid_names)
def test_40_change_reglament_name(login_reglaments, name):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/name",
        json={
            "name": name,
        },
    )
    assert response.status_code == 200


@allure.title("PATCH /reglaments/reglament_id/name")
@pytest.mark.parametrize("name", invalid_names)
def test_41_change_reglament_name(login_reglaments, name):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/name",
        json={
            "name": name,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/name")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_42_change_reglament_name(login_reglaments, reglament_id):
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/name",
        json={
            "name": "string",
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/name")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_43_change_reglament_name(login_reglaments, reglament_id):
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/name",
        json={
            "name": "string",
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/content")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_44_change_reglament_content(login_reglaments, reglament_id):
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/content",
        json={
            "content": "string",
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/content")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_45_change_reglament_name(login_reglaments, reglament_id):
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/content",
        json={
            "content": "string",
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /reglaments/reglament_id/content")
def test_46_change_reglament_name(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.patch(
        HOST + f"/reglaments/{reglament_id}/content",
        json={
            "content": "string",
        },
    )
    assert response.status_code == 200


@allure.title("POST /reglaments/reglament_id/history")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_47_change_reglament_history(login_reglaments, reglament_id):
    response = login_reglaments.post(
        HOST + f"/reglaments/{reglament_id}/history",
        json={
            "comment": "string",
        },
    )
    assert response.status_code == 400


@allure.title("POST /reglaments/reglament_id/history")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_48_change_reglament_history(login_reglaments, reglament_id):
    response = login_reglaments.post(
        HOST + f"/reglaments/{reglament_id}/history",
        json={
            "comment": "string",
        },
    )
    assert response.status_code == 400


@allure.title("POST /reglaments/reglament_id/history")
def test_49_change_reglament_history(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.post(
        HOST + f"/reglaments/{reglament_id}/history",
        json={
            "comment": "string",
        },
    )
    assert response.status_code == 201


@allure.title("GET /reglaments/reglament_id/history")
def test_50_get_reglament_history(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.get(HOST + f"/reglaments/{reglament_id}/history")
    assert response.status_code == 200


@allure.title("GET /reglaments/reglament_id/history")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_51_get_reglament_history(login_reglaments, reglament_id):
    response = login_reglaments.get(HOST + f"/reglaments/{reglament_id}/history")
    assert response.status_code == 400


@allure.title("GET /reglaments/reglament_id/history")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_52_get_reglament_history(login_reglaments, reglament_id):
    response = login_reglaments.get(HOST + f"/reglaments/{reglament_id}/history")
    assert response.status_code == 400


@allure.title("POST /reglaments/reglament_id/complete-intro")
def test_53_reglament_complete_intro(login_reglaments):
    reglament = login_reglaments.get(HOST + "/reglaments").json()[0]
    reglament_id = reglament["id"]
    response = login_reglaments.post(
        HOST + f"/reglaments/{reglament_id}/complete-intro"
    )
    assert response.status_code == 201


@allure.title("POST /reglaments/reglament_id/complete-intro")
@pytest.mark.parametrize("reglament_id", invalid_space_id)
def test_54_reglament_complete_intro(login_reglaments, reglament_id):
    response = login_reglaments.post(
        HOST + f"/reglaments/{reglament_id}/complete-intro"
    )
    assert response.status_code == 400


@allure.title("POST /reglaments/reglament_id/complete-intro")
@pytest.mark.parametrize("reglament_id", valid_ids)
def test_55_reglament_complete_intro(login_reglaments, reglament_id):
    response = login_reglaments.post(
        HOST + f"/reglaments/{reglament_id}/complete-intro"
    )
    assert response.status_code == 400
