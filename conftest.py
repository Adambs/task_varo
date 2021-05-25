import pytest


@pytest.fixture(autouse=True)
def get_auth_token():
    import requests
    import json

    url = "http://0.0.0.0:8000/api/auth"

    payload = json.dumps({
        "username": "test",
        "password": "1234"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {your_token_here}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data_loaded = json.loads(response.text)

    token = data_loaded['access_token']

    return token

    # print(response.text)
    #
    # return response
