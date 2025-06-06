from utils.api_helpers import get_with_token

def test_fetch_user_profile(base_url, auth_token):
    profile_endpoint = f"{base_url}/user/profile"
    response = get_with_token(profile_endpoint, auth_token)

    assert response.status_code == 200
    data = response.json()

    assert "username" in data
    assert "email" in data

