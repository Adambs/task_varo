import json

import requests


def test_get_poly(get_auth_token):
    # test to do:
    # status code
    # empty list return empty array   - if i could delete all by api I could create this state

    token = get_auth_token

    url = "http://0.0.0.0:8000/api/poly"

    payload = json.dumps({
        "username": "test",
        "password": "1234"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)

    assert response.status_code == 200


def test_get_poly_count_number_of_elements(get_auth_token):
    # valid number of elements

    token = get_auth_token

    url = "http://0.0.0.0:8000/api/poly"

    payload = json.dumps({
        "username": "test",
        "password": "1234"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data_loaded = json.loads(response.text)

    number_of_elements_returned_list = len(data_loaded)

    assert number_of_elements_returned_list == 2  # ideal way to get the expected value is to do a db query


def test_post_poly(get_auth_token):
    # status code
    # returned object is same as was sent in body
    # handle invalid input

    url = "http://0.0.0.0:8000/api/poly"

    token = get_auth_token

    object_to_create = {
        "data": [
            {
                "key": "key1",
                "val": "val1",
                "valType": "str"
            }
        ]
    }

    payload = json.dumps(object_to_create)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    assert response.status_code == 200


def test_post_poly_verify_object_values(get_auth_token):
    # returned object is same as was sent in body

    url = "http://0.0.0.0:8000/api/poly"

    token = get_auth_token


    object_to_create = {
        "data": [
            {
                "key": "key1",
                "val": "val1",
                "valType": "str"
            }
        ]
    }

    payload = json.dumps(object_to_create)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    object_returned_from_server = json.loads(response.text)

    res_key = object_returned_from_server['values'][0]['key']

    res_val = object_returned_from_server['values'][0]['val']

    res_valType = object_returned_from_server['values'][0]['valType']

    assert (object_to_create["data"][0]["key"] == res_key) and (object_to_create["data"][0]["val"] == res_val) \
           and (object_to_create["data"][0]["valType"] == res_valType)


def test_post_poly_bad_request(get_auth_token):
    # handle invalid input
    url = "http://0.0.0.0:8000/api/poly"

    token = get_auth_token

    payload = json.dumps({
        "data": [
            {
                "key": "key1",
                "val4": "val1",
                "valType": "str"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    assert response.status_code == 400


def test_get_object_by_id(get_auth_token):
    # valid status code
    # valid object structure
    # handle invalid input
    # invalid input

    token = get_auth_token

    object_template = {
        "data": [
            {
                "key": "key1",
                "val": "val1",
                "valType": "str"
            }
        ]
    }

    url = "http://0.0.0.0:8000/api/poly/2"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    object_returned_from_server = json.loads(response.text)

    res_key = object_returned_from_server['data'][0]['key']

    res_val = object_returned_from_server['data'][0]['val']

    res_valType = object_returned_from_server['data'][0]['valType']

    assert (object_template["data"][0]["key"] == res_key) and (object_template["data"][0]["val"] == res_val) \
           and (object_template["data"][0]["valType"] == res_valType)


def test_delete_object_by_id(get_auth_token):
    # valid status code

    url = "http://0.0.0.0:8000/api/poly/1"

    token = get_auth_token

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    assert response.status_code == 204


def test_delete_not_existing_object(get_auth_token):
    # delete not existing object

    url = "http://0.0.0.0:8000/api/poly/7#"

    token = get_auth_token

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    assert response.status_code == 404

