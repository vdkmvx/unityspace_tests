import allure
import pytest
from data.getenv import HOST
from data.data import invalid_names, valid_names, invalid_space_id


@allure.title("GET /projects/all-projects")
def test_get_projects(login_projects):
    response = login_projects.get(HOST + "/projects/all-projects")
    assert response.status_code == 200


@allure.title("POST /projects")
@pytest.mark.parametrize("name", invalid_names)
def test_create_project_with_invalid_name(login_projects, name):
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
@pytest.mark.parametrize("space_column_id", invalid_space_id)
def test_create_project_with_invalid_space_column_id(login_projects, space_column_id):
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
def test_create_project_with_invalid_responsible_id(login_projects, responsible_id):
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
@pytest.mark.parametrize("responsible_id", invalid_space_id)
def test_create_project_with_invalid_post_task_day_count(
    login_projects, responsible_id
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
            "postponingTaskDayCount": -5,
        },
    )
    assert response.status_code == 400
