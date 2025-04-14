import requests

def test_get_user_with_body():
    """✅ Ответ с телом — получение пользователя"""
    response = requests.get("https://reqres.in/api/users/2")
    body = response.json()
    assert response.status_code == 200
    assert "data" in body
    assert body["data"]["id"] == 2
    assert body["data"]["email"] == "janet.weaver@reqres.in"

def test_delete_user_without_body():
    """✅ Ответ без тела — удаление пользователя"""
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204
    assert response.text == ""  # Ответ пустой