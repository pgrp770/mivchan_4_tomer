import pytest
from flask import Flask
from controller.target_controller import target_blueprint
from model import Target


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(target_blueprint)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_target_by_id_api(client):
    response = client.get('/1')
    assert response.status_code == 200


def test_all_targets_api(client):
    response = client.get('/')
    assert response.status_code == 200


def test_create_target_api(client):
    target = {"coordinates_id": 1,
              "location_id": 1,
              "type_id": 1,
              "industry_id": 1,
              "priority": 1,
              "mission_id": 2
              }
    response = client.post('/create', json=target)
    assert response.status_code == 200
