import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_greeting_returns_hello_wissen(client):
    response = client.get('/api/greeting')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello Wissen'}

def test_greeting_method_not_allowed(client):
    response = client.post('/api/greeting')
    assert response.status_code == 405

def test_not_found(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404