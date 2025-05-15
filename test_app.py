from app import app
import pytest

def test_hello():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b'Hello, DevOps!'
        assert response.status_code == 200