from rest import app
from flask import json


def test_get():
    response = app.test_client().get('/v1/groceries',
    content_type='application/json'
    )
    assert response.status_code==200

def test_use():
    response = app.test_client().get('/v1/users?userID=MILAN',
    content_type='application/json'
    )
    assert response.status_code==200

def test_add():
    response = app.test_client().post('/v1/groceries',
    data = json.dumps({'name':'Nachos'}),
    content_type='application/json',
    headers=({'userID':'Brittney'})
    )
    assert response.status_code == 200

def test_put():
    response = app.test_client().put('/v1/groceries?ID=1213',
    data = json.dumps({'name':'Rainbow'}),
    headers=({'userID':'Milan'}),
    content_type='application/json',
    
    )
    assert response.status_code == 200


def test_delete():
    response = app.test_client().delete('/v1/groceries?ID=1213',
    data = json.dumps({'name':'Rainbow'}),
    content_type='application/json',
    )
    assert response.status_code == 200

