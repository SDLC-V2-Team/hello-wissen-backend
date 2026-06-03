import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_greeting_happy_path(client):
    resp = client.get('/api/greeting')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data == {'message': 'hello wissen'}

def test_greeting_method_not_allowed(client):
    resp = client.post('/api/greeting')
    assert resp.status_code == 405

def test_greeting_not_found(client):
    resp = client.get('/nonexistent')
    assert resp.status_code == 404

def test_greeting_content_type(client):
    resp = client.get('/api/greeting')
    assert resp.headers['Content-Type'] == 'application/json'