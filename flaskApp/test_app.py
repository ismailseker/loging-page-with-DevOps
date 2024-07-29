import pytest
from app import app, db
from flask import jsonify

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        db.drop_all()

def test_login(client):
    response = client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert 'Set-Cookie' in response.headers

def test_register(client):
    response = client.post('/register', json={'username': 'newuser', 'password': 'newpass', 'email': 'newuser@example.com'})
    assert response.status_code == 200
    assert b'You have successfully registered!' in response.data

def test_home_authenticated(client):
    client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
    response = client.get('/home', cookies={'session': 'testsession'})
    assert response.status_code == 200
    assert b'Welcome, testuser' in response.data
