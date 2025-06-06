import requests

def get_with_token(url, token):
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(url, headers=headers)

def post_with_token(url, token, payload):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    return requests.post(url, headers=headers, json=payload)

