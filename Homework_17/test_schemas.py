import requests
from jsonschema import validate
from schemasHW import (
    get_single_user_schema,
    create_user_schema,
    update_user_schema,
    error_schema,
)

def test_get_user_schema():
    response = requests.get("https://reqres.in/api/users/2")
    body = response.json()
    assert response.status_code == 200
    validate(body, get_single_user_schema)

def test_post_user_schema():
    payload = {"name": "Morpheus", "job": "Zion leader"}
    response = requests.post("https://reqres.in/api/users", json=payload)
    body = response.json()
    assert response.status_code == 201
    validate(body, create_user_schema)

def test_put_user_schema():
    payload = {"name": "Neo", "job": "The One"}
    response = requests.put("https://reqres.in/api/users/2", json=payload)
    body = response.json()
    assert response.status_code == 200
    validate(body, update_user_schema)

def test_register_negative_schema():
    payload = {"email": "sydney@fife"}  # no password
    response = requests.post("https://reqres.in/api/register", json=payload)
    body = response.json()
    assert response.status_code == 400
    validate(body, error_schema)