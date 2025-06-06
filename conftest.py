import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://api.example.com"

@pytest.fixture(scope="session")
def credentials():
    return {"username": "user1", "password": "pass123"}

@pytest.fixture(scope="session")
def auth_token(base_url, credentials):
    login_endpoint = f"{base_url}/login"
    response = requests.post(login_endpoint, json=credentials)
    assert response.status_code == 200
    return response.json().get("access_token")

