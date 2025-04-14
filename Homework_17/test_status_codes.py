import requests

def test_status_code_200():
    """✅ 200 OK — успешный GET"""
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200

def test_status_code_201():
    """✅ 201 Created — успешный POST"""
    payload = {"name": "Agent Smith", "job": "AI"}
    response = requests.post("https://reqres.in/api/users", json=payload)
    assert response.status_code == 201

def test_status_code_204():
    """✅ 204 No Content — успешный DELETE"""
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204
    assert response.text == ""

def test_status_code_404():
    """❌ 404 Not Found — несуществующий ресурс"""
    response = requests.get("https://reqres.in/api/unknown/23")
    assert response.status_code == 404

def test_status_code_400():
    """❌ 400 Bad Request — ошибка регистрации без пароля"""
    payload = {"email": "sydney@fife"}  # без password
    response = requests.post("https://reqres.in/api/register", json=payload)
    assert response.status_code == 400
    assert "error" in response.json()