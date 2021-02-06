
import json
import requests

URL = 'http://127.0.0.1:5000'


def test_post_page():
    data = {'name': 'Machine'}
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain', 'userID': 'Milan'}
    testing_post_request = requests.post(URL + '/v1/groceries',
            data=json.dumps(data), headers=headers)  # Assumses that it has a path of "/"
    assert testing_post_request.status_code == 200  # Assumes that it will return a 200 responsed


def test_get_page():
    data = {'name': 'Machine'}
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain'}
    testing_get_request = requests.get(URL + '/v1/groceries',
            data=json.dumps(data), headers=headers)  # Assumses that it has a path of "/"
    assert testing_get_request.status_code == 200  # Assumes that it will return a 200 responsed


def test_user_page():
    data = {'userID': 'Milan'}
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain'}
    testing_user_request = requests.get(URL + '/v1/users',
            params=data, headers=headers)  # Assumses that it has a path of "/"
    assert testing_user_request.status_code == 200  # Assumes that it will return a 200 responsed

def test_put_page():
    data = {'name': 'Fried Chicken'}
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain', 'userID': 'Milan'}
    testing_put_request = requests.put(URL + '/v1/groceries',
            data=json.dumps(data), headers=headers)  # Assumses that it has a path of "/"
    assert testing_put_request.status_code == 200  # Assumes that it will return a 200 responsed


def test_delete_page():
    data = {'name': 'Fried Chicken'}
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain', 'userID': 'Milan'}
    testing_delete_request = requests.delete(URL + '/v1/groceries',
            data=json.dumps(data), headers=headers)  # Assumses that it has a path of "/"
    assert testing_delete_request.status_code == 200  # Assumes that it will return a 200 responsed
