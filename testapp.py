
import json
import requests



url = 'http://127.0.0.1:5000'

def test_post_page():
     data = {'name': 'Machine'}
     headers = {'Content-type': 'application/json', 'Accept': 'text/plain','userID':'Milan'}
     r = requests.post(url + '/v1/groceries',data=json.dumps(data),headers=headers) # Assumses that it has a path of "/"
     assert r.status_code == 200 # Assumes that it will return a 200 responsed

def test_get_page():
     data = {'name': 'Machine'}
     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
     r = requests.get(url + '/v1/groceries',data=json.dumps(data),headers=headers) # Assumses that it has a path of "/"
     assert r.status_code == 200 # Assumes that it will return a 200 responsed


def test_user_page():
     data = {'userID': 'Milan'}
     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
     r = requests.get(url + '/v1/users',params=data,headers=headers) # Assumses that it has a path of "/"
     assert r.status_code == 200 # Assumes that it will return a 200 responsed
     

def test_put_page():
     data = {'name': 'Fried Chicken'}
     headers = {'Content-type': 'application/json', 'Accept': 'text/plain','userID':'Milan'}
     r = requests.put(url + '/v1/groceries/createdBy',data=json.dumps(data),headers=headers) # Assumses that it has a path of "/"
     assert r.status_code == 200 # Assumes that it will return a 200 responsed

def test_delete_page():
     data = {'name': 'Fried Chicken'}
     headers = {'Content-type': 'application/json', 'Accept': 'text/plain','userID':'Milan'}
     r = requests.delete(url + '/v1/groceries',data=json.dumps(data),headers=headers) # Assumses that it has a path of "/"
     assert r.status_code == 200 # Assumes that it will return a 200 responsed