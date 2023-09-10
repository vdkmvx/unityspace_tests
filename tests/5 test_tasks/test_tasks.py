from data.getenv import HOST
from data.data import (
    invalid_space_id,
    valid_ids,
    valid_names,
    invalid_names,
    valid_orders,
    invalid_orders,
)
from data.time import time_now
import allure
import pytest


@allure.title("GET /tasks")
def test_1_get_tasks(login_tasks):
    response = login_tasks.get(HOST + "/tasks")
    assert response.status_code == 200


@allure.title("POST /tasks")
@pytest.mark.parametrize("stage_id", invalid_space_id)
def test_2_create_task(login_tasks, stage_id):
    response = login_tasks.post(
        HOST + "/tasks",
        json={
            "name": "string",
            "stageId": stage_id,
            "order": 0,
            "responsibleUserId": None,
            "description": "string",
            "color": "string",
            "dateBegin": time_now(),
            "dateEnd": time_now(),
        },
    )
    assert response.status_code == 400


@allure.title("POST /tasks")
@pytest.mark.parametrize("stage_id", valid_ids)
def test_3_create_task(login_tasks, stage_id):
    response = login_tasks.post(
        HOST + "/tasks",
        json={
            "name": "string",
            "stageId": stage_id,
            "order": 0,
            "responsibleUserId": None,
            "description": "string",
            "color": "string",
            "dateBegin": time_now(),
            "dateEnd": time_now(),
        },
    )
    assert response.status_code == 400


@allure.title("POST /tasks")
@pytest.mark.parametrize("name", valid_names)
def test_4_create_task(login_tasks, name):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.post(
        HOST + "/tasks",
        json={
            "name": name,
            "stageId": project_stage_id,
            "order": 0,
            "responsibleUserId": None,
            "description": "string",
            "color": "string",
            "dateBegin": time_now(),
            "dateEnd": time_now(),
        },
    )
    assert response.status_code == 201


@allure.title("POST /tasks")
@pytest.mark.parametrize("name", invalid_names)
def test_5_create_task(login_tasks, name):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.post(
        HOST + "/tasks",
        json={
            "name": name,
            "stageId": project_stage_id,
            "order": 0,
            "responsibleUserId": None,
            "description": "string",
            "color": "string",
            "dateBegin": time_now(),
            "dateEnd": time_now(),
        },
    )
    assert response.status_code == 400


@allure.title("POST /tasks")
@pytest.mark.parametrize("order", invalid_orders)
def test_6_create_task(login_tasks, order):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.post(
        HOST + "/tasks",
        json={
            "name": "Задача",
            "stageId": project_stage_id,
            "order": order,
            "responsibleUserId": None,
            "description": "string",
            "color": "string",
            "dateBegin": time_now(),
            "dateEnd": time_now(),
        },
    )
    assert response.status_code == 400


@allure.title("POST /tasks")
@pytest.mark.parametrize("order", valid_orders)
def test_7_create_task(login_tasks, order):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.post(
        HOST + "/tasks",
        json={
            "name": "Задача",
            "stageId": project_stage_id,
            "order": order,
            "responsibleUserId": None,
            "description": "string",
            "color": "string",
            "dateBegin": time_now(),
            "dateEnd": time_now(),
        },
    )
    assert response.status_code == 201


@allure.title("POST /tasks")
@pytest.mark.parametrize("space_member_id", invalid_orders)
def test_8_create_task(login_tasks, space_member_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.post(
        HOST + "/tasks",
        json={
            "name": "Задача",
            "stageId": project_stage_id,
            "order": 0,
            "responsibleUserId": space_member_id,
            "description": "string",
            "color": "string",
            "dateBegin": time_now(),
            "dateEnd": time_now(),
        },
    )
    assert response.status_code == 400


@allure.title("POST /tasks")
@pytest.mark.parametrize("space_member_id", valid_orders)
def test_9_create_task(login_tasks, space_member_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.post(
        HOST + "/tasks",
        json={
            "name": "Задача",
            "stageId": project_stage_id,
            "order": 0,
            "responsibleUserId": space_member_id,
            "description": "string",
            "color": "string",
            "dateBegin": time_now(),
            "dateEnd": time_now(),
        },
    )
    assert response.status_code == 400


@allure.title("POST /tasks")
def test_10_create_task(login_tasks):
    space = login_tasks.get(HOST + "/spaces").json()[0]
    space_member_id = space["members"][0]["id"]
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.post(
        HOST + "/tasks",
        json={
            "name": "Задача",
            "stageId": project_stage_id,
            "order": 0,
            "responsibleUserId": space_member_id,
            "description": "string",
            "color": "string",
            "dateBegin": time_now(),
            "dateEnd": time_now(),
        },
    )
    assert response.status_code == 201


@allure.title("POST /tasks")  # невалидная дата
def test_11_create_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.post(
        HOST + "/tasks",
        json={
            "name": "Задача",
            "stageId": project_stage_id,
            "order": 0,
            "responsibleUserId": None,
            "description": "string",
            "color": "string",
            "dateBegin": "abc",
            "dateEnd": "abc",
        },
    )
    assert response.status_code == 400


@allure.title("GET /tasks/myHistory/page")
@pytest.mark.parametrize("page", valid_ids)
def test_12_create_task(login_tasks, page):
    response = login_tasks.post(HOST + f"/tasks/myHistory/{page}")
    assert response.status_code == 404


@allure.title("GET /tasks/myHistory/page")
@pytest.mark.parametrize("page", invalid_space_id)
def test_13_create_task(login_tasks, page):
    response = login_tasks.post(HOST + f"/tasks/myHistory/{page}")
    assert response.status_code == 404
