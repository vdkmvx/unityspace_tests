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
def test_12_get_my_history(login_tasks, page):
    response = login_tasks.post(HOST + f"/tasks/myHistory/{page}")
    assert response.status_code == 404


@allure.title("GET /tasks/myHistory/page")
@pytest.mark.parametrize("page", invalid_space_id)
def test_13_get_my_history(login_tasks, page):
    response = login_tasks.post(HOST + f"/tasks/myHistory/{page}")
    assert response.status_code == 404


@pytest.mark.skip("Шо это такое")
@allure.title("POST /tasks/duplicate")
def test_14_duplicate_task():
    pass


@allure.title("POST /tasks/move")
def test_15_task_move(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.post(
        HOST + "/tasks/move", json={"stageId": project_stage_id, "taskIds": [task_id]}
    )
    assert response.status_code == 201


@allure.title("POST /tasks/move")
@pytest.mark.parametrize("project_stage_id", invalid_space_id)
def test_16_task_move(login_tasks, project_stage_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.post(
        HOST + "/tasks/move", json={"stageId": project_stage_id, "taskIds": [task_id]}
    )
    assert response.status_code == 400


@allure.title("POST /tasks/move")
@pytest.mark.parametrize("project_stage_id", valid_ids)
def test_17_task_move(login_tasks, project_stage_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.post(
        HOST + "/tasks/move", json={"stageId": project_stage_id, "taskIds": [task_id]}
    )
    assert response.status_code == 400


@allure.title("POST /tasks/move")
@pytest.mark.parametrize("task_id", valid_ids)
def test_18_task_move(login_tasks, task_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.post(
        HOST + "/tasks/move", json={"stageId": project_stage_id, "taskIds": [task_id]}
    )
    assert response.status_code == 400


@allure.title("POST /tasks/move")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_19_task_move(login_tasks, task_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.post(
        HOST + "/tasks/move", json={"stageId": project_stage_id, "taskIds": [task_id]}
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/complete")
def test_20_task_complete(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + "/tasks/complete",
        json={"stageId": project_stage_id, "tasksIds": [task_id]},
    )
    assert response.status_code == 200


@allure.title("PATCH /tasks/complete")
@pytest.mark.parametrize("project_stage_id", invalid_space_id)
def test_21_task_complete(login_tasks, project_stage_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + "/tasks/complete",
        json={"stageId": project_stage_id, "tasksIds": [task_id]},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/complete")
@pytest.mark.parametrize("project_stage_id", valid_ids)
def test_22_task_complete(login_tasks, project_stage_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + "/tasks/complete",
        json={"stageId": project_stage_id, "tasksIds": [task_id]},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/complete")
@pytest.mark.parametrize("task_id", valid_ids)
def test_23_task_complete(login_tasks, task_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.patch(
        HOST + "/tasks/complete",
        json={"stageId": project_stage_id, "tasksIds": [task_id]},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/complete")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_24_task_complete(login_tasks, task_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.patch(
        HOST + "/tasks/complete",
        json={"stageId": project_stage_id, "tasksIds": [task_id]},
    )
    assert response.status_code == 400


@allure.title("DELETE /tasks/task_id")
def test_25_delete_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.delete(HOST + f"/tasks/{task_id}")
    assert response.status_code == 200


@allure.title("DELETE /tasks/task_id")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_26_delete_task(login_tasks, task_id):
    response = login_tasks.delete(HOST + f"/tasks/{task_id}")
    assert response.status_code == 400


@allure.title("DELETE /tasks/task_id")
@pytest.mark.parametrize("task_id", valid_ids)
def test_27_delete_task(login_tasks, task_id):
    response = login_tasks.delete(HOST + f"/tasks/{task_id}")
    assert response.status_code == 400


@allure.title("GET /tasks/task_id")
def test_28_get_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.get(HOST + f"/tasks/{task_id}")
    assert response.status_code == 200


@allure.title("GET /tasks/task_id")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_29_get_task(login_tasks, task_id):
    response = login_tasks.get(HOST + f"/tasks/{task_id}")
    assert response.status_code == 400


@allure.title("GET /tasks/task_id")
@pytest.mark.parametrize("task_id", valid_ids)
def test_30_get_task(login_tasks, task_id):
    response = login_tasks.get(HOST + f"/tasks/{task_id}")
    assert response.status_code == 403


@allure.title("POST /tasks/task_id/tag/tag_id")
def test_31_add_tag_to_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    tag = login_tasks.get(HOST + "/tags").json()[0]
    tag_id = tag["id"]
    response = login_tasks.post(HOST + f"/tasks/{task_id}/tag/{tag_id}")
    assert response.status_code == 201


@allure.title("POST /tasks/task_id/tag/tag_id")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_32_add_tag_to_task(login_tasks, task_id):
    tag = login_tasks.get(HOST + "/tags").json()[0]
    tag_id = tag["id"]
    response = login_tasks.post(HOST + f"/tasks/{task_id}/tag/{tag_id}")
    assert response.status_code == 400


@allure.title("POST /tasks/task_id/tag/tag_id")
@pytest.mark.parametrize("task_id", valid_ids)
def test_33_add_tag_to_task(login_tasks, task_id):
    tag = login_tasks.get(HOST + "/tags").json()[0]
    tag_id = tag["id"]
    response = login_tasks.post(HOST + f"/tasks/{task_id}/tag/{tag_id}")
    assert response.status_code == 400


@allure.title("POST /tasks/task_id/tag/tag_id")
@pytest.mark.parametrize("tag_id", valid_ids)
def test_34_add_tag_to_task(login_tasks, tag_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.post(HOST + f"/tasks/{task_id}/tag/{tag_id}")
    assert response.status_code == 400


@allure.title("POST /tasks/task_id/tag/tag_id")
@pytest.mark.parametrize("tag_id", invalid_space_id)
def test_35_add_tag_to_task(login_tasks, tag_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.post(HOST + f"/tasks/{task_id}/tag/{tag_id}")
    assert response.status_code == 400


@allure.title("Непонятный запрос PATCH /tasks/task_id/tag/tag_id")
def test_36_delete_tag_from_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    tag = login_tasks.get(HOST + "/tags").json()[0]
    tag_id = tag["id"]
    response = login_tasks.patch(HOST + f"/tasks/{task_id}/tag/{tag_id}")
    assert response.status_code == 200


@allure.title("Непонятный запрос PATCH /tasks/task_id/tag/tag_id")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_37_delete_tag_from_task(login_tasks, task_id):
    tag = login_tasks.get(HOST + "/tags").json()[0]
    tag_id = tag["id"]
    response = login_tasks.patch(HOST + f"/tasks/{task_id}/tag/{tag_id}")
    assert response.status_code == 400


@allure.title("Непонятный запрос PATCH /tasks/task_id/tag/tag_id")
@pytest.mark.parametrize("task_id", valid_ids)
def test_38_delete_tag_from_task(login_tasks, task_id):
    tag = login_tasks.get(HOST + "/tags").json()[0]
    tag_id = tag["id"]
    response = login_tasks.patch(HOST + f"/tasks/{task_id}/tag/{tag_id}")
    assert response.status_code == 400


@allure.title("Непонятный запрос PATCH /tasks/task_id/tag/tag_id")
@pytest.mark.parametrize("tag_id", valid_ids)
def test_39_delete_tag_from_task(login_tasks, tag_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(HOST + f"/tasks/{task_id}/tag/{tag_id}")
    assert response.status_code == 400


@allure.title("Непонятный запрос PATCH /tasks/task_id/tag/tag_id")
@pytest.mark.parametrize("tag_id", invalid_space_id)
def test_40_delete_tag_from_task(login_tasks, tag_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(HOST + f"/tasks/{task_id}/tag/{tag_id}")
    assert response.status_code == 400
