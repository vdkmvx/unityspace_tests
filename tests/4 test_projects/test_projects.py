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
    invalid_project_limit,
    boolean,
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


@allure.title("DELETE /projects/project_id/stages/stage_id")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_47_delete_stage_into_invalid_project(login_projects, project_id):
    response = login_projects.delete(HOST + f"/projects/{project_id}/stages/1")
    assert response.status_code == 400


@allure.title("DELETE /projects/project_id/stages/stage_id")
@pytest.mark.parametrize("project_id", valid_ids)
def test_48_delete_stage_into_invalid_project(login_projects, project_id):
    response = login_projects.delete(HOST + f"/projects/{project_id}/stages/1")
    assert response.status_code == 400


@allure.title("DELETE /projects/project_id/stages/stage_id")
@pytest.mark.parametrize("stage_id", invalid_space_id)
def test_49_delete_invalid_stage_into_project(login_projects, stage_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.delete(HOST + f"/projects/{project_id}/stages/{stage_id}")
    assert response.status_code == 400


@allure.title("DELETE /projects/project_id/stages/stage_id")
@pytest.mark.parametrize("stage_id", valid_ids)
def test_50_delete_invalid_stage_into_project(login_projects, stage_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.delete(HOST + f"/projects/{project_id}/stages/{stage_id}")
    assert response.status_code == 400


@allure.title("DELETE /projects/project_id/stages/stage_id")
def test_51_delete_invalid_stage_into_project(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    response = login_projects.delete(
        HOST + f"/projects/{project_id}/stages/{project_stage_id}"
    )
    assert response.status_code == 200


@allure.title("DELETE /projects/project_id/stages/stage_id")
@pytest.mark.parametrize("stage_id", valid_ids)
def test_50_delete_invalid_stage_into_project(login_projects, stage_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.delete(HOST + f"/projects/{project_id}/stages/{stage_id}")
    assert response.status_code == 400


@allure.title("DELETE /projects/project_id/stages/stage_id")
def test_51_delete_invalid_stage_into_project(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    response = login_projects.delete(
        HOST + f"/projects/{project_id}/stages/{project_stage_id}"
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id/stages/stage_id")
@pytest.mark.parametrize("name", valid_names)
def test_52_change_name_stage_into_project(login_projects, name):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/{project_stage_id}", json={"name": name}
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id/stages/stage_id")
@pytest.mark.parametrize("name", invalid_names)
def test_53_change_invalid_name_stage_into_project(login_projects, name):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/{project_stage_id}", json={"name": name}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/stages/stage_id")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_54_change_name_stage_into_invalid_project(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/1", json={"name": "Колонка"}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/stages/stage_id")
@pytest.mark.parametrize("project_id", valid_ids)
def test_55_change_name_stage_into_invalid_project(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/1", json={"name": "Колонка"}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/stages/stage_id")
@pytest.mark.parametrize("project_stage_id", valid_ids)
def test_56_change_name_invalid_stage_into_project(login_projects, project_stage_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/{project_stage_id}",
        json={"name": "Колонка"},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/stages/stage_id")
@pytest.mark.parametrize("project_stage_id", invalid_space_id)
def test_57_change_name_invalid_stage_into_project(login_projects, project_stage_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/{project_stage_id}",
        json={"name": "Колонка"},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/stages/stage_id/limit")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_58_change_project_stage_limit_with_invalid_project(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/1/limit", json={"taskLimit": None}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/stages/stage_id/limit")
@pytest.mark.parametrize("project_id", valid_ids)
def test_59_change_project_stage_limit_with_invalid_project(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/1/limit", json={"taskLimit": None}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/stages/stage_id/limit")
@pytest.mark.parametrize("project_stage_id", valid_ids)
def test_60_change_project_stage_limit_with_invalid_project_stage(
    login_projects, project_stage_id
):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/{project_stage_id}/limit",
        json={"taskLimit": None},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/stages/stage_id/limit")
@pytest.mark.parametrize("project_stage_id", invalid_space_id)
def test_61_change_project_stage_limit_with_invalid_project_stage(
    login_projects, project_stage_id
):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/{project_stage_id}/limit",
        json={"taskLimit": None},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/stages/stage_id/limit")
@pytest.mark.parametrize("task_limit", valid_ids)
def test_62_change_project_stage_limit(login_projects, task_limit):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/{project_stage_id}/limit",
        json={"taskLimit": task_limit},
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id/stages/stage_id/limit")
@pytest.mark.parametrize("task_limit", invalid_project_limit)
def test_63_change_project_stage_limit(login_projects, task_limit):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/stages/{project_stage_id}/limit",
        json={"taskLimit": task_limit},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/updateStageOrder/stage_id")
def test_64_update_stage_order(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/updateStageOrder/{project_stage_id}", json={"order": 1}
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/updateStageOrder/stage_id")
@pytest.mark.parametrize("project_stage_id", invalid_space_id)
def test_64_update_stage_order_with_invalid_stage_id(login_projects, project_stage_id):
    response = login_projects.patch(
        HOST + f"/projects/updateStageOrder/{project_stage_id}", json={"order": 1}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/updateStageOrder/stage_id")
@pytest.mark.parametrize("project_stage_id", valid_ids)
def test_65_update_stage_order_with_invalid_stage_id(login_projects, project_stage_id):
    response = login_projects.patch(
        HOST + f"/projects/updateStageOrder/{project_stage_id}", json={"order": 1}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/updateStageOrder/stage_id")
@pytest.mark.parametrize("order", invalid_orders)
def test_66_update_stage_order_with_invalid_order(login_projects, order):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/updateStageOrder/{project_stage_id}",
        json={"order": invalid_orders},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/updateProjectStage/moveProject")
def test_67_update_project_stage(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_stage_id = project["stages"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/updateProjectStage/moveProject",
        json={"stageId": project_stage_id, "newProjectId": project_id},
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/updateProjectStage/moveProject")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_68_update_project_stage(login_projects, project_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/updateProjectStage/moveProject",
        json={"stageId": project_stage_id, "newProjectId": project_id},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/updateProjectStage/moveProject")
@pytest.mark.parametrize("project_id", valid_ids)
def test_69_update_project_stage(login_projects, project_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_stage_id = project["stages"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/updateProjectStage/moveProject",
        json={"stageId": project_stage_id, "newProjectId": project_id},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/updateProjectStage/moveProject")
@pytest.mark.parametrize("project_stage_id", valid_ids)
def test_70_update_project_stage(login_projects, project_stage_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/updateProjectStage/moveProject",
        json={"stageId": project_stage_id, "newProjectId": project_id},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/updateProjectStage/moveProject")
@pytest.mark.parametrize("project_stage_id", invalid_space_id)
def test_71_update_project_stage(login_projects, project_stage_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/updateProjectStage/moveProject",
        json={"stageId": project_stage_id, "newProjectId": project_id},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/showProjectReviewTab")
@pytest.mark.parametrize("show", boolean)
def test_72_show_project_review_tab(login_projects, show):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/showProjectReviewTab",
        json={
            "show": show,
        },
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id/showProjectReviewTab")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_73_show_project_review_tab(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/showProjectReviewTab",
        json={
            "show": True,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/showProjectReviewTab")
@pytest.mark.parametrize("project_id", valid_ids)
def test_74_show_project_review_tab(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/showProjectReviewTab",
        json={
            "show": True,
        },
    )
    assert response.status_code == 400


@allure.title("GET /projects/project_id/tasks")
def test_75_get_tasks_into_project(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.get(HOST + f"/projects/{project_id}/tasks")
    assert response.status_code == 200


@allure.title("GET /projects/project_id/tasks")
@pytest.mark.parametrize("project_id", valid_ids)
def test_76_get_tasks_into_project(login_projects, project_id):
    response = login_projects.get(HOST + f"/projects/{project_id}/tasks")
    assert response.status_code == 400


@allure.title("GET /projects/project_id/tasks")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_77_get_tasks_into_project(login_projects, project_id):
    response = login_projects.get(HOST + f"/projects/{project_id}/tasks")
    assert response.status_code == 400


@allure.title("GET /projects/project_id/archiveTasks/page")
def test_78_get_archive_task_into_project(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.get(HOST + f"/projects/{project_id}/archiveTasks/1")
    assert response.status_code == 200


@allure.title("GET /projects/project_id/archiveTasks/page")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_79_get_archive_task_into_project(login_projects, project_id):
    response = login_projects.get(HOST + f"/projects/{project_id}/archiveTasks/1")
    assert response.status_code == 400


@allure.title("GET /projects/project_id/archiveTasks/page")
@pytest.mark.parametrize("project_id", valid_ids)
def test_80_get_archive_task_into_project(login_projects, project_id):
    response = login_projects.get(HOST + f"/projects/{project_id}/archiveTasks/1")
    assert response.status_code == 400


@allure.title("GET /projects/project_id/archiveTasks/page")
@pytest.mark.parametrize("page", valid_ids)
def test_81_get_archive_task_into_project(login_projects, page):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.get(HOST + f"/projects/{project_id}/archiveTasks/{page}")
    assert response.status_code == 200


@allure.title("GET /projects/project_id/archiveTasks/page")
@pytest.mark.parametrize("page", invalid_space_id)
def test_82_get_archive_task_into_project(login_projects, page):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.get(HOST + f"/projects/{project_id}/archiveTasks/{page}")
    assert response.status_code == 400


@allure.title("GET /projects/project_id/storageTasks/page")
def test_83_get_storage_task_into_project(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.get(HOST + f"/projects/{project_id}/storageTasks/1")
    assert response.status_code == 200


@allure.title("GET /projects/project_id/storageTasks/page")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_84_get_storage_task_into_project(login_projects, project_id):
    response = login_projects.get(HOST + f"/projects/{project_id}/storageTasks/1")
    assert response.status_code == 400


@allure.title("GET /projects/project_id/storageTasks/page")
@pytest.mark.parametrize("project_id", valid_ids)
def test_85_get_storage_task_into_project(login_projects, project_id):
    response = login_projects.get(HOST + f"/projects/{project_id}/storageTasks/1")
    assert response.status_code == 400


@allure.title("GET /projects/project_id/storageTasks/page")
@pytest.mark.parametrize("page", valid_ids)
def test_86_get_storage_task_into_project(login_projects, page):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.get(HOST + f"/projects/{project_id}/archiveTasks/{page}")
    assert response.status_code == 200


@allure.title("GET /projects/project_id/storageTasks/page")
@pytest.mark.parametrize("page", invalid_space_id)
def test_87_get_storage_task_into_project(login_projects, page):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.get(HOST + f"/projects/{project_id}/storageTasks/{page}")
    assert response.status_code == 400


@allure.title("POST /projects/project_id/embed")
def test_88_create_embed(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.post(
        HOST + f"/projects/{project_id}/embed",
        json={"category": "string", "name": "string", "url": "https://unityspace.ru"},
    )
    assert response.status_code == 201


@allure.title("POST /projects/project_id/embed")
def test_88_create_embed(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.post(
        HOST + f"/projects/{project_id}/embed",
        json={"category": "string", "name": "string", "url": "https://unityspace.ru"},
    )
    assert response.status_code == 201


@allure.title("POST /projects/project_id/embed")
@pytest.mark.parametrize("project_id", valid_ids)
def test_89_create_embed(login_projects, project_id):
    response = login_projects.post(
        HOST + f"/projects/{project_id}/embed",
        json={"category": "string", "name": "string", "url": "https://unityspace.ru"},
    )
    assert response.status_code == 400


@allure.title("POST /projects/project_id/embed")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_90_create_embed(login_projects, project_id):
    response = login_projects.post(
        HOST + f"/projects/{project_id}/embed",
        json={"category": "string", "name": "string", "url": "https://unityspace.ru"},
    )
    assert response.status_code == 400


@allure.title("POST /projects/project_id/embed")
@pytest.mark.parametrize("name", valid_names)
def test_91_create_embed(login_projects, name):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.post(
        HOST + f"/projects/{project_id}/embed",
        json={"category": "string", "name": name, "url": "https://unityspace.ru"},
    )
    assert response.status_code == 201


@allure.title("POST /projects/project_id/embed")
@pytest.mark.parametrize("name", invalid_names)
def test_92_create_embed(login_projects, name):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.post(
        HOST + f"/projects/{project_id}/embed",
        json={"category": "string", "name": name, "url": "https://unityspace.ru"},
    )
    assert response.status_code == 400


@allure.title("POST /projects/project_id/embed")
def test_93_create_embed(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.post(
        HOST + f"/projects/{project_id}/embed",
        json={"category": "string", "name": "name", "url": "unityspace.ru"},
    )
    assert response.status_code == 400


@allure.title("POST /projects/project_id/embed")
@pytest.mark.parametrize("category", invalid_names)
def test_94_create_embed(login_projects, category):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.post(
        HOST + f"/projects/{project_id}/embed",
        json={"category": category, "name": "name", "url": "unityspace.ru"},
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/changeEmbedOrder/embed_id/order")
@pytest.mark.parametrize("order", valid_orders)
def test_95_change_embed_order(login_projects, order):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_embed_id = project["embeddings"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/changeEmbedOrder/{project_embed_id}/order",
        json={
            "order": order,
        },
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/changeEmbedOrder/embed_id/order")
@pytest.mark.parametrize("order", invalid_orders)
def test_96_change_embed_order(login_projects, order):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_embed_id = project["embeddings"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/changeEmbedOrder/{project_embed_id}/order",
        json={
            "order": order,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/changeEmbedOrder/embed_id/order")
@pytest.mark.parametrize("project_embed_id", invalid_space_id)
def test_97_change_embed_order(login_projects, project_embed_id):
    response = login_projects.patch(
        HOST + f"/projects/changeEmbedOrder/{project_embed_id}/order",
        json={
            "order": 1,
        },
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/changeEmbedOrder/embed_id/order")
@pytest.mark.parametrize("project_embed_id", valid_ids)
def test_98_change_embed_order(login_projects, project_embed_id):
    response = login_projects.patch(
        HOST + f"/projects/changeEmbedOrder/{project_embed_id}/order",
        json={
            "order": 1,
        },
    )
    assert response.status_code == 400


@allure.title("DELETE /projects/project_id/embed/embed_id")
def test_99_delete_embed(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    project_embed_id = project["embeddings"][0]["id"]
    response = login_projects.delete(
        HOST + f"/projects/{project_id}/embed/{project_embed_id}"
    )
    assert response.status_code == 200


@allure.title("DELETE /projects/project_id/embed/embed_id")
@pytest.mark.parametrize("project_id", valid_ids)
def test_100_delete_embed(login_projects, project_id):
    response = login_projects.delete(HOST + f"/projects/{project_id}/embed/1")
    assert response.status_code == 400


@allure.title("DELETE /projects/project_id/embed/embed_id")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_101_delete_embed(login_projects, project_id):
    response = login_projects.delete(HOST + f"/projects/{project_id}/embed/1")
    assert response.status_code == 400


@allure.title("DELETE /projects/project_id/embed/embed_id")
@pytest.mark.parametrize("project_embed_id", invalid_space_id)
def test_102_delete_embed(login_projects, project_embed_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.delete(
        HOST + f"/projects/{project_id}/embed/{project_embed_id}"
    )
    assert response.status_code == 400


@allure.title("DELETE /projects/project_id/embed/embed_id")
@pytest.mark.parametrize("project_embed_id", valid_ids)
def test_103_delete_embed(login_projects, project_embed_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.delete(
        HOST + f"/projects/{project_id}/embed/{project_embed_id}"
    )
    assert response.status_code == 400


@pytest.mark.skip(reason="Запрос надо поправить")
@allure.title("PATCH /projects/{projectId}/embed/{embedId}")
def test_104_change_embed():
    pass


@allure.title("PATCH /projects/project_id/changeColumn/column_id")
def test_105_change_project_into_new_column(login_projects):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/changeColumn/{space_column_id}"
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id/changeColumn/column_id")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_106_change_project_into_new_column(login_projects, project_id):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/changeColumn/{space_column_id}"
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/changeColumn/column_id")
@pytest.mark.parametrize("project_id", valid_ids)
def test_107_change_project_into_new_column(login_projects, project_id):
    space = login_projects.get(HOST + "/spaces").json()[0]
    space_column_id = space["columns"][0]["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/changeColumn/{space_column_id}"
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/changeColumn/column_id")
@pytest.mark.parametrize("space_column_id", valid_ids)
def test_108_change_project_into_new_column(login_projects, space_column_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/changeColumn/{space_column_id}"
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/changeColumn/column_id")
@pytest.mark.parametrize("space_column_id", invalid_space_id)
def test_109_change_project_into_new_column(login_projects, space_column_id):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/changeColumn/{space_column_id}"
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/changeTimelineViewType")
@pytest.mark.parametrize("type", boolean)
def test_110_change_project_into_new_column(login_projects, type):
    project = login_projects.get(HOST + "/projects/all-projects").json()[0]
    project_id = project["id"]
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/changeTimelineViewType", json={"type": type}
    )
    assert response.status_code == 200


@allure.title("PATCH /projects/project_id/changeTimelineViewType")
@pytest.mark.parametrize("project_id", valid_ids)
def test_111_change_project_into_new_column(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/changeTimelineViewType", json={"type": True}
    )
    assert response.status_code == 400


@allure.title("PATCH /projects/project_id/changeTimelineViewType")
@pytest.mark.parametrize("project_id", invalid_space_id)
def test_112_change_project_into_new_column(login_projects, project_id):
    response = login_projects.patch(
        HOST + f"/projects/{project_id}/changeTimelineViewType", json={"type": True}
    )
    assert response.status_code == 400
