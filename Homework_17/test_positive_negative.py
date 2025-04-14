import requests


def test_create_user_positive():
    """✅ Позитивный: создание пользователя с валидными данными"""
    payload = {"name": "Trinity", "job": "Hacker"}
    response = requests.post("https://reqres.in/api/users", json=payload)
    body = response.json()

    assert response.status_code == 201
    assert body["name"] == "Trinity"
    assert body["job"] == "Hacker"
    assert "id" in body
    assert "createdAt" in body

def test_create_user_negative_no_name():
    """❌ Негативный: отправка без имени"""
    payload = {"job": "Hacker"}  # name отсутствует
    response = requests.post("https://reqres.in/api/users", json=payload)
    body = response.json()

    assert response.status_code == 201  # API не валидирует поля жёстко
    assert "id" in body
    assert "createdAt" in body
    assert "name" not in body  # ожидаем, что name не отразится

def test_create_user_negative_empty_payload():
    """❌ Негативный: пустой запрос"""
    response = requests.post("https://reqres.in/api/users", json={})
    body = response.json()

    assert response.status_code == 201  # reqres всё равно создаёт юзера
    assert "id" in body
    assert "createdAt" in body