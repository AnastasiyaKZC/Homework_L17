import requests

def test_create_user():
    """✅ Проверка создания пользователя: возвращается id и createdAt"""
    name = "morpheus"
    job = "leader"

    payload = {"name": name, "job": job}
    response = requests.post("https://reqres.in/api/users", json=payload)
    body = response.json()

    # Проверка статуса ответа
    assert response.status_code == 201

    # Проверка, что в ответе есть name и job
    assert body["name"] == name
    assert body["job"] == job

    # Проверка, что ответ содержит id и createdAt
    assert "id" in body
    assert "createdAt" in body