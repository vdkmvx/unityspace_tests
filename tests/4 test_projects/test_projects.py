import allure
import pytest
from data.getenv import HOST
from data.data import (
    invalid_names,
    valid_names,
    invalid_space_id,
    valid_ids,
    invalid_post_task_day_count,
    valid_orders,
    invalid_orders,
)


@allure.title("GET /projects/all-projects")
def test_1_get_projects(login_projects):
    response = login_projects.get(HOST + "/projects/all-projects")
    assert response.status_code == 200


@allure.title("POST /projects")
@pytest.mark.parametrize("name", invalid_names)
def test_2_create_project_with_invalid_name(login_projects, name):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    response = login_projects.post(
        HOST + "/projects",
        json={
            "name": name,
            "spaceColumnId": space_column_id,
            "color": "string",
            "responsibleId": None,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 400


@allure.title("POST /projects")
@pytest.mark.parametrize("name", valid_names)
def test_3_create_project(login_projects, name):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    response = login_projects.post(
        HOST + "/projects",
        json={
            "name": name,
            "spaceColumnId": space_column_id,
            "color": "string",
            "responsibleId": None,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 201


@allure.title("POST /projects")
@pytest.mark.parametrize("space_column_id", invalid_space_id)
def test_4_create_project_with_invalid_space_column_id(login_projects, space_column_id):
    response = login_projects.post(
        HOST + "/projects",
        json={
            "name": "Проект",
            "spaceColumnId": space_column_id,
            "color": "string",
            "responsibleId": None,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 400


@allure.title("POST /projects")
@pytest.mark.parametrize("space_column_id", valid_ids)
def test_5_create_project_with_invalid_space_column_id(login_projects, space_column_id):
    response = login_projects.post(
        HOST + "/projects",
        json={
            "name": "Проект",
            "spaceColumnId": space_column_id,
            "color": "string",
            "responsibleId": None,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 400


@allure.title("POST /projects")
@pytest.mark.parametrize("responsible_id", invalid_space_id)
def test_6_create_project_with_invalid_responsible_id(login_projects, responsible_id):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    response = login_projects.post(
        HOST + "/projects",
        json={
            "name": "Проект2",
            "spaceColumnId": space_column_id,
            "color": "string",
            "responsibleId": responsible_id,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 400


@allure.title("POST /projects")
@pytest.mark.parametrize("responsible_id", valid_ids)
def test_7_create_project_with_invalid_responsible_id(login_projects, responsible_id):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    response = login_projects.post(
        HOST + "/projects",
        json={
            "name": "Проект2",
            "spaceColumnId": space_column_id,
            "color": "string",
            "responsibleId": responsible_id,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 400


@allure.title("POST /projects")
def test_8_create_project_with_valid_responsible_id(login_projects):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    space_member_id = space["members"][0]["id"]
    response = login_projects.post(
        HOST + "/projects",
        json={
            "name": "Проект2",
            "spaceColumnId": space_column_id,
            "color": "string",
            "responsibleId": space_member_id,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 201


@allure.title("POST /projects")
@pytest.mark.parametrize("post_task_day_count", invalid_post_task_day_count)
def test_9_create_project_with_invalid_post_task_day_count(
    login_projects, post_task_day_count
):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    response = login_projects.post(
        HOST + "/projects",
        json={
            "name": "Проект2",
            "spaceColumnId": space_column_id,
            "color": "string",
            "responsibleId": None,
            "postponingTaskDayCount": post_task_day_count,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id")
def test_10_change_project(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}",
        json={
            "name": "Name",
            "color": "string",
            "responsibleId": None,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id")
@pytest.mark.parametrize("name", invalid_names)
def test_11_change_project_with_invalid_name(login_projects, name):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}",
        json={
            "name": name,
            "color": "string",
            "responsibleId": None,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_12_change_project_with_invalid_project_id(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}",
        json={
            "name": "Проект",
            "color": "string",
            "responsibleId": None,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id")
@pytest.mark.parametrize("project_id", valid_ids)
def test_13_change_project_with_invalid_project_id(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}",
        json={
            "name": "Проект",
            "color": "string",
            "responsibleId": None,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id")
@pytest.mark.parametrize("responsible_id", invalid_space_id)
def test_14_change_project_with_invalid_responsible_id(login_projects, responsible_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}",
        json={
            "name": "Проект",
            "color": "string",
            "responsibleId": responsible_id,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id")
@pytest.mark.parametrize("responsible_id", valid_ids)
def test_15_change_project_with_invalid_responsible_id(login_projects, responsible_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}",
        json={
            "name": "Проект",
            "color": "string",
            "responsibleId": responsible_id,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id")
def test_16_change_project_with_valid_responsible_id(login_projects):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_member_id = space["members"][0]["id"]
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}",
        json={
            "name": "Проект",
            "color": "string",
            "responsibleId": space_member_id,
            "postponingTaskDayCount": 0,
        },
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id")
@pytest.mark.parametrize("post_task_day_count", invalid_post_task_day_count)
def test_17_change_project_with_invalid_post_task_day_count(
    login_projects, post_task_day_count
):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_member_id = space["members"][0]["id"]
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}",
        json={
            "name": "Проект",
            "color": "string",
            "responsibleId": space_member_id,
            "postponingTaskDayCount": post_task_day_count,
        },
    )
    assert response.status_code == 400


@allure.title("GET /projects/project_id")
def test_18_get_project(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.get(HOST + f"/projects/{project_id}")
    assert response.status_code == 200


@allure.title("GET /projects/project_id")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_19_get_project_with_invalid_id(login_projects, project_id):
    response = login_projects.get(HOST + f"/projects/{project_id}")
    assert response.status_code == 400


@allure.title("GET /projects/project_id")
@pytest.mark.parametrize("project_id", valid_ids)
def test_20_get_project_with_invalid_id(login_projects, project_id):
    response = login_projects.get(HOST + f"/projects/{project_id}")
    assert response.status_code == 400


@allure.title("DELETE /projects/project_id")
def test_21_get_project(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.delete(HOST + f"/projects/{project_id}")
    assert response.status_code == 200


@allure.title("DELETE /projects/project_id")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_22_get_project_with_invalid_id(login_projects, project_id):
    response = login_projects.delete(HOST + f"/projects/{project_id}")
    assert response.status_code == 400


@allure.title("DELETE /projects/project_id")
@pytest.mark.parametrize("project_id", valid_ids)
def test_23_get_project_with_invalid_id(login_projects, project_id):
    response = login_projects.delete(HOST + f"/projects/{project_id}")
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/memo")
def test_24_change_project_memo(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/memo", json={"memo": "string"}
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id/memo")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_25_get_change_project_memo_with_invalid_project_id(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/memo", json={"memo": "string"}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/memo")
@pytest.mark.parametrize("project_id", valid_ids)
def test_26_get_change_project_memo_with_invalid_project_id(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/memo", json={"memo": "string"}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/move")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_27_move_project_with_invalid_id(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/move", json={"columnId": 0, "order": 0}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/move")
@pytest.mark.parametrize("project_id", valid_ids)
def test_28_move_project_with_invalid_id(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/move", json={"columnId": 0, "order": 0}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/move")
@pytest.mark.parametrize("space_column_id", valid_ids)
def test_29_move_project_with_invalid_column_id(login_projects, space_column_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/move",
        json={"columnId": space_column_id, "order": 0},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/move")
@pytest.mark.parametrize("space_column_id", invalid_space_id)
def test_30_move_project_with_invalid_column_id(login_projects, space_column_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/move",
        json={"columnId": space_column_id, "order": 0},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/move")
def test_31_move_project(login_projects):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/move",
        json={"columnId": space_column_id, "order": 0},
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id/move")
@pytest.mark.parametrize("space_column_order", valid_orders)
def test_32_move_project(login_projects, space_column_order):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/move",
        json={"columnId": space_column_id, "order": space_column_order},
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id/move")
@pytest.mark.parametrize("space_column_order", invalid_orders)
def test_33_move_project_with_invalid_orders(login_projects, space_column_order):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/move",
        json={"columnId": space_column_id, "order": space_column_order},
    )
    assert response.status_code == 400


@allure.title("POST /projects/project_id/stages")
@pytest.mark.parametrize("name", valid_names)
def test_34_create_stage_into_project(login_projects, name):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.post(
        HOST + f"/projects/{project_id}/stages",
        json={"name": name, "order": 0, "tasks": []},
    )
    assert response.status_code == 201


@allure.title("POST /projects/project_id/stages")
@pytest.mark.parametrize("name", invalid_names)
def test_35_create_stage_into_project_with_invalid_name(login_projects, name):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.post(
        HOST + f"/projects/{project_id}/stages",
        json={"name": name, "order": 0, "tasks": []},
    )
    assert response.status_code == 400


@allure.title("POST /projects/project_id/stages")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_36_create_stage_into_project_with_invalid_project_id(
    login_projects, project_id
):
    response = login_projects.post(
        HOST + f"/projects/{project_id}/stages",
        json={"name": "Колонка", "order": 0, "tasks": []},
    )
    assert response.status_code == 400


@allure.title("POST /projects/project_id/stages")
@pytest.mark.parametrize("project_id", valid_ids)
def test_37_create_stage_into_project_with_invalid_project_id(
    login_projects, project_id
):
    response = login_projects.post(
        HOST + f"/projects/{project_id}/stages",
        json={"name": "Колонка", "order": 0, "tasks": []},
    )
    assert response.status_code == 400


@allure.title("POST /projects/project_id/stages")
@pytest.mark.parametrize("order", invalid_orders)
def test_38_create_stage_into_project_with_invalid_order(login_projects, order):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.post(
        HOST + f"/projects/{project_id}/stages",
        json={"name": "Колонка", "order": order, "tasks": []},
    )
    assert response.status_code == 400


@allure.title("POST /projects/project_id/stages")
@pytest.mark.parametrize("task", invalid_space_id)
def test_39_create_stage_into_project_with_invalid_task(login_projects, task):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.post(
        HOST + f"/projects/{project_id}/stages",
        json={"name": "Колонка", "order": 0, "tasks": [task]},
    )
    assert response.status_code == 400


@allure.title("POST /projects/project_id/stages")
@pytest.mark.parametrize("task", valid_ids)
def test_40_create_stage_into_project_with_invalid_task(login_projects, task):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.post(
        HOST + f"/projects/{project_id}/stages",
        json={"name": "Колонка", "order": 0, "tasks": [task]},
    )
    assert response.status_code == 400


@allure.title("GET /projects/project_id/description")
@pytest.mark.parametrize("project_id", valid_ids)
def test_41_get_project_description_with_invalid_id(login_projects, project_id):
    response = login_projects.get(HOST + f"/projects/{project_id}/description")
    assert response.status_code == 400


@allure.title("GET /projects/project_id/description")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_42_get_project_description_with_invalid_id(login_projects, project_id):
    response = login_projects.get(HOST + f"/projects/{project_id}/description")
    assert response.status_code == 400


@allure.title("GET /projects/project_id/description")
def test_43_get_project_description(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.get(HOST + f"/projects/{project_id}/description")
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id/description")
def test_44_change_project_description(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/description", json={"description": ""}
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id/description")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_45_change_project_description_with_invalid_project_id(
    login_projects, project_id
):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/description", json={"description": ""}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/description")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_46_change_project_description_with_invalid_project_id(
    login_projects, project_id
):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/description", json={"description": ""}
    )
    assert response.status_code == 400
