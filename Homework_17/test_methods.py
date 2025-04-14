import requests

def test_get_user():
    """GET: Получение пользователя"""
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    assert "data" in response.json()
    assert response.json()["data"]["id"] == 2

def test_post_user():
    """POST: Создание нового пользователя"""
    payload = {"name": "Neo", "job": "The One"}
    response = requests.post("https://reqres.in/api/users", data=payload)
    body = response.json()

    assert response.status_code == 201
    assert body["name"] == "Neo"
    assert "id" in body
    assert "createdAt" in body

def test_put_user():
    """PUT: Обновление информации о пользователе"""
    payload = {"name": "Neo", "job": "Zion Savior"}
    response = requests.put("https://reqres.in/api/users/2", data=payload)
    body = response.json()

    assert response.status_code == 200
    assert body["name"] == "Neo"
    assert body["job"] == "Zion Savior"
    assert "updatedAt" in body

def test_delete_user():
    """DELETE: Удаление пользователя"""
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204
    assert response.text == ""
    
    
    