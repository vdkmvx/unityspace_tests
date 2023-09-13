from data.getenv import HOST
from data.data import (
    invalid_space_id,
    valid_ids,
    valid_names,
    invalid_names,
    valid_orders,
    invalid_orders,
    invalid_post_task_day_count,
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


@allure.title("PATCH /tasks/task_id/description")
def test_41_change_description_into_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/description",
        json={"description": "<p>string</p>", "descriptionText": "string"},
    )
    assert response.status_code == 200


@allure.title("PATCH /tasks/task_id/description")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_42_change_description_into_task(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/description",
        json={"description": "string", "descriptionText": "string"},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/description")
@pytest.mark.parametrize("task_id", valid_ids)
def test_43_change_description_into_task(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/description",
        json={"description": "string", "descriptionText": "string"},
    )
    assert response.status_code == 400


@allure.title("GET /tasks/task_id/description")
def test_44_get_description_into_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.get(HOST + f"/tasks/{task_id}/description")
    assert response.status_code == 200


@allure.title("GET /tasks/task_id/description")
@pytest.mark.parametrize("task_id", valid_ids)
def test_45_get_description_into_task(login_tasks, task_id):
    response = login_tasks.get(HOST + f"/tasks/{task_id}/description")
    assert response.status_code == 400


@allure.title("GET /tasks/task_id/description")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_46_get_description_into_task(login_tasks, task_id):
    response = login_tasks.get(HOST + f"/tasks/{task_id}/description")
    assert response.status_code == 400


@allure.title("PATCH /tasks/updateTaskName/task_id")
@pytest.mark.parametrize("name", valid_names)
def test_47_change_name_into_task(login_tasks, name):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskName/{task_id}", json={"name": name}
    )
    assert response.status_code == 200


@allure.title("PATCH /tasks/updateTaskName/task_id")
@pytest.mark.parametrize("name", invalid_names)
def test_48_change_name_into_task(login_tasks, name):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskName/{task_id}", json={"name": name}
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/updateTaskName/task_id")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_49_change_name_into_task(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskName/{task_id}", json={"name": "123"}
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/updateTaskName/task_id")
@pytest.mark.parametrize("task_id", valid_ids)
def test_50_change_name_into_task(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskName/{task_id}", json={"name": "123"}
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/blockReason")
def test_51_block_reason_for_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/blockReason", json={"blockReason": ""}
    )
    assert response.status_code == 200


@allure.title("PATCH /tasks/task_id/blockReason")
@pytest.mark.parametrize("task_id", valid_ids)
def test_52_block_reason_for_task(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/blockReason", json={"blockReason": ""}
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/blockReason")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_53_block_reason_for_task(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/blockReason", json={"blockReason": ""}
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/updateTaskResponsible/task_id")
def test_54_update_task_responsible(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    space = login_tasks.get(HOST + "/spaces").json()[0]
    space_member_id = space["members"][0]["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskResponsible/{task_id}",
        json={"responsibleId": space_member_id},
    )
    assert response.status_code == 200


@allure.title("PATCH /tasks/updateTaskResponsible/task_id")
@pytest.mark.parametrize("space_member_id", invalid_space_id)
def test_55_update_task_responsible(login_tasks, space_member_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskResponsible/{task_id}",
        json={"responsibleId": space_member_id},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/updateTaskResponsible/task_id")
@pytest.mark.parametrize("space_member_id", valid_ids)
def test_56_update_task_responsible(login_tasks, space_member_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskResponsible/{task_id}",
        json={"responsibleId": space_member_id},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/updateTaskResponsible/task_id")
@pytest.mark.parametrize("task_id", valid_ids)
def test_57_update_task_responsible(login_tasks, task_id):
    space = login_tasks.get(HOST + "/spaces").json()[0]
    space_member_id = space["members"][0]["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskResponsible/{task_id}",
        json={"responsibleId": space_member_id},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/updateTaskResponsible/task_id")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_58_update_task_responsible(login_tasks, task_id):
    space = login_tasks.get(HOST + "/spaces").json()[0]
    space_member_id = space["members"][0]["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskResponsible/{task_id}",
        json={"responsibleId": space_member_id},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/updateTaskColor/task_id")
def test_59_update_task_color(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskColor/{task_id}", json={"color": ""}
    )
    assert response.status_code == 200


@allure.title("PATCH /tasks/updateTaskColor/task_id")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_60_update_task_color(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskColor/{task_id}", json={"color": ""}
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/updateTaskColor/task_id")
@pytest.mark.parametrize("task_id", valid_ids)
def test_61_update_task_color(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/updateTaskColor/{task_id}", json={"color": ""}
    )
    assert response.status_code == 400


@allure.title("GET /tasks/task_id/history")
def test_62_get_task_history(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.get(HOST + f"/tasks/{task_id}/history")
    assert response.status_code == 200


@allure.title("GET /tasks/task_id/history")
@pytest.mark.parametrize("task_id", valid_ids)
def test_63_get_task_history(login_tasks, task_id):
    response = login_tasks.get(HOST + f"/tasks/{task_id}/history")
    assert response.status_code == 400


@allure.title("GET /tasks/task_id/history")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_64_get_task_history(login_tasks, task_id):
    response = login_tasks.get(HOST + f"/tasks/{task_id}/history")
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/changeColumnAndOrder")
def test_65_change_order_and_column_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeColumnAndOrder",
        json={"stageId": project_stage_id, "order": 0},
    )
    assert response.status_code == 200


@allure.title("PATCH /tasks/task_id/changeColumnAndOrder")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_66_change_order_and_column_task(login_tasks, task_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeColumnAndOrder",
        json={"stageId": project_stage_id, "order": 0},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/changeColumnAndOrder")
@pytest.mark.parametrize("task_id", valid_ids)
def test_67_change_order_and_column_task(login_tasks, task_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeColumnAndOrder",
        json={"stageId": project_stage_id, "order": 0},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/changeColumnAndOrder")
@pytest.mark.parametrize("project_stage_id", valid_ids)
def test_68_change_order_and_column_task(login_tasks, project_stage_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeColumnAndOrder",
        json={"stageId": project_stage_id, "order": 0},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/changeColumnAndOrder")
@pytest.mark.parametrize("project_stage_id", invalid_space_id)
def test_69_change_order_and_column_task(login_tasks, project_stage_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeColumnAndOrder",
        json={"stageId": project_stage_id, "order": 0},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/changeColumnAndOrder")
@pytest.mark.parametrize("order", valid_orders)
def test_70_change_order_and_column_task(login_tasks, order):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeColumnAndOrder",
        json={"stageId": project_stage_id, "order": order},
    )
    assert response.status_code == 200


@allure.title("PATCH /tasks/task_id/changeColumnAndOrder")
@pytest.mark.parametrize("order", invalid_orders)
def test_71_change_order_and_column_task(login_tasks, order):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeColumnAndOrder",
        json={"stageId": project_stage_id, "order": order},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/changeTaskDate")
def test_72_change_task_date(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeTaskDate",
        json={"dateBegin": time_now(), "dateEnd": time_now()},
    )
    assert response.status_code == 200


@allure.title("PATCH /tasks/task_id/changeTaskDate")
def test_73_change_task_date(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeTaskDate",
        json={"dateBegin": "string", "dateEnd": "string"},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/changeTaskDate")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_74_change_task_date(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeTaskDate",
        json={"dateBegin": time_now(), "dateEnd": time_now()},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/changeTaskDate")
@pytest.mark.parametrize("task_id", valid_ids)
def test_75_change_task_date(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeTaskDate",
        json={"dateBegin": time_now(), "dateEnd": time_now()},
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/changeTaskStatus")
def test_76_change_task_status(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeTaskStatus",
        json={
            "status": 0,
        },
    )
    assert response.status_code == 200


@allure.title("PATCH /tasks/task_id/changeTaskStatus")
@pytest.mark.parametrize("status", invalid_post_task_day_count)
def test_77_change_task_status(login_tasks, status):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeTaskStatus",
        json={
            "status": status,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/changeTaskStatus")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_78_change_task_status(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeTaskStatus",
        json={
            "status": 0,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/changeTaskStatus")
@pytest.mark.parametrize("task_id", valid_ids)
def test_79_change_task_status(login_tasks, task_id):
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/changeTaskStatus",
        json={
            "status": 0,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/add-member")
def test_80_add_member_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    space = login_tasks.get(HOST + "/spaces").json()[0]
    space_member_id = space["members"][0]["id"]
    response = login_tasks.post(
        HOST + f"/tasks/{task_id}/add-member", json={"userIds": [space_member_id]}
    )
    assert response.status_code == 201


@allure.title("PATCH /tasks/task_id/add-member")
@pytest.mark.parametrize("space_member_id", invalid_space_id)
def test_81_add_member_task(login_tasks, space_member_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.post(
        HOST + f"/tasks/{task_id}/add-member", json={"userIds": [space_member_id]}
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/add-member")
@pytest.mark.parametrize("space_member_id", valid_ids)
def test_82_add_member_task(login_tasks, space_member_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.post(
        HOST + f"/tasks/{task_id}/add-member", json={"userIds": [space_member_id]}
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/add-member")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_83_add_member_task(login_tasks, task_id):
    space = login_tasks.get(HOST + "/spaces").json()[0]
    space_member_id = space["members"][0]["id"]
    response = login_tasks.post(
        HOST + f"/tasks/{task_id}/add-member", json={"userIds": [space_member_id]}
    )
    assert response.status_code == 400


@allure.title("PATCH /tasks/task_id/add-member")
@pytest.mark.parametrize("task_id", valid_ids)
def test_84_add_member_task(login_tasks, task_id):
    space = login_tasks.get(HOST + "/spaces").json()[0]
    space_member_id = space["members"][0]["id"]
    response = login_tasks.post(
        HOST + f"/tasks/{task_id}/add-member", json={"userIds": [space_member_id]}
    )
    assert response.status_code == 400


@allure.title("DELETE /tasks/task_id/remove-member/user_id")
def test_85_add_member_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    user_id = task["members"][0]
    response = login_tasks.delete(HOST + f"/tasks/{task_id}/remove-member/{user_id}")
    assert response.status_code == 200


@allure.title("DELETE /tasks/task_id/remove-member/user_id")
@pytest.mark.parametrize("task_id", valid_ids)
def test_86_add_member_task(login_tasks, task_id):
    response = login_tasks.delete(HOST + f"/tasks/{task_id}/remove-member/1")
    assert response.status_code == 400


@allure.title("DELETE /tasks/task_id/remove-member/user_id")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_87_add_member_task(login_tasks, task_id):
    response = login_tasks.delete(HOST + f"/tasks/{task_id}/remove-member/1")
    assert response.status_code == 400


@allure.title("DELETE /tasks/task_id/remove-member/user_id")
@pytest.mark.parametrize("user_id", invalid_space_id)
def test_88_add_member_task(login_tasks, user_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.delete(HOST + f"/tasks/{task_id}/remove-member/{user_id}")
    assert response.status_code == 400


@allure.title("DELETE /tasks/task_id/remove-member/user_id")
@pytest.mark.parametrize("user_id", valid_ids)
def test_89_add_member_task(login_tasks, user_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.delete(HOST + f"/tasks/{task_id}/remove-member/{user_id}")
    assert response.status_code == 400


@pytest.mark.skip(reason="Не разобрался с загрузкой файлов")
@allure.title("PUT /tasks/task_id/cover")
def test_90_put_cover_task(login_tasks):
    pass


@allure.title("DELETE /tasks/task_id/cover")
def test_91_delete_cover_task(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.delete(HOST + f"/tasks/{task_id}/cover")
    assert response.status_code == 200


@allure.title("DELETE /tasks/task_id/cover")
@pytest.mark.parametrize("task_id", valid_ids)
def test_92_delete_cover_task(login_tasks, task_id):
    response = login_tasks.delete(HOST + f"/tasks/{task_id}/cover")
    assert response.status_code == 400


@allure.title("DELETE /tasks/task_id/cover")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_93_delete_cover_task(login_tasks, task_id):
    response = login_tasks.delete(HOST + f"/tasks/{task_id}/cover")
    assert response.status_code == 400


@allure.title("GET /tasks/task_id/messages")
def test_94_get_task_messages(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.get(HOST + f"/tasks/{task_id}/messages")
    assert response.status_code == 200


@allure.title("GET /tasks/task_id/messages")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_95_get_task_messages(login_tasks, task_id):
    response = login_tasks.get(HOST + f"/tasks/{task_id}/messages")
    assert response.status_code == 400


@allure.title("GET /tasks/task_id/messages")
@pytest.mark.parametrize("task_id", valid_ids)
def test_96_get_task_messages(login_tasks, task_id):
    response = login_tasks.get(HOST + f"/tasks/{task_id}/messages")
    assert response.status_code == 400


@allure.title("POST /tasks/task_id/messages")
def test_97_post_task_messages(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.post(
        HOST + f"/tasks/{task_id}/messages",
        json={
            "text": "string",
            "files": [],
        },
    )
    assert response.status_code == 201


@allure.title("POST /tasks/task_id/messages")
def test_98_post_task_messages(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.post(
        HOST + f"/tasks/{task_id}/messages",
        json={
            "text": "",
            "files": [],
        },
    )
    assert response.status_code == 400


@allure.title("POST /tasks/task_id/messages")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_99_post_task_messages(login_tasks, task_id):
    response = login_tasks.post(
        HOST + f"/tasks/{task_id}/messages",
        json={
            "text": "string",
            "files": [],
        },
    )
    assert response.status_code == 400


@allure.title("POST /tasks/task_id/messages")
@pytest.mark.parametrize("task_id", valid_ids)
def test_100_post_task_messages(login_tasks, task_id):
    response = login_tasks.post(
        HOST + f"/tasks/{task_id}/messages",
        json={
            "text": "string",
            "files": [],
        },
    )
    assert response.status_code == 400


@pytest.mark.skip(reason="Скип")
def test_101_patch_message():
    pass


@allure.title("POST /tasks/task_id/messages/message_id/deleted")
def test_102_delete_message(login_tasks):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    task_message = login_tasks.get(HOST + f"/tasks/{task_id}/messages").json()[0]
    task_message_id = task_message["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/messages/{task_message_id}/deleted"
    )
    assert response.status_code == 200


@allure.title("POST /tasks/task_id/messages/message_id/deleted")
@pytest.mark.parametrize("task_id", valid_ids)
def test_103_delete_message(login_tasks, task_id):
    response = login_tasks.patch(HOST + f"/tasks/{task_id}/messages/1/deleted")
    assert response.status_code == 400


@allure.title("POST /tasks/task_id/messages/message_id/deleted")
@pytest.mark.parametrize("task_id", invalid_space_id)
def test_104_delete_message(login_tasks, task_id):
    response = login_tasks.patch(HOST + f"/tasks/{task_id}/messages/1/deleted")
    assert response.status_code == 400


@allure.title("POST /tasks/task_id/messages/message_id/deleted")
@pytest.mark.parametrize("task_message_id", invalid_space_id)
def test_105_delete_message(login_tasks, task_message_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/messages/{task_message_id}/deleted"
    )
    assert response.status_code == 400


@allure.title("POST /tasks/task_id/messages/message_id/deleted")
@pytest.mark.parametrize("task_message_id", valid_ids)
def test_106_delete_message(login_tasks, task_message_id):
    project = login_tasks.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    task = login_tasks.get(HOST + f"/projects/{project_id}/tasks").json()[0]
    task_id = task["id"]
    response = login_tasks.patch(
        HOST + f"/tasks/{task_id}/messages/{task_message_id}/deleted"
    )
    assert response.status_code == 400
