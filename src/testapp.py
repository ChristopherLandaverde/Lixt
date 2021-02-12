#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
import requests

URL = 'http://127.0.0.1:5000'



@pytest.mark.server(url='/v1/groceries/', response=[{'name': 'Machine'
                    }], method='POST')
def test_handler_responses():
    response = requests.post(URL + '/v1/groceries/', timeout=1)
    assert response.status_code == 200


@pytest.mark.server(url='/v1/groceries/', response=[{'name': 'Machine'
                    }], method='GET')
def test_post_responses():
    response = requests.get('http://127.0.0.1:5000' + '/v1/groceries')
    assert response.status_code == 200
    assert response.json() == [{'name': 'Machine'}]


@pytest.mark.server(url='/v1/users/', response=[{'userID': 'Milan'}],
                    method='GET')
def test_user_responses():
    response = requests.get(URL + '/v1/users/')
    assert response.status_code == 200
    assert response.json() == [{'userID': 'Milan'}]


@pytest.mark.server(url='/v1/groceries/', response=[{'name': 'Machine'
                    }], method='DELETE')
def test_delete_responses():
    response = requests.get(URL + '/v1/groceries/')
    assert response.status_code == 200
    assert response.json() == [{'name': 'Machine'}]


@pytest.mark.server(url='/v1/groceries/',
                    response=[{'name': 'Fried Chicken',
                    'userID': 'Milan'}], method='PUT')
def test_put_responses():
    response = requests.put(URL + '/v1/groceries/')
    assert response.status_code == 200
    assert response.json() == [{'name': 'Fried Chicken',
                               'userID': 'Milan'}]
