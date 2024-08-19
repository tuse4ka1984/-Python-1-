import requests
import allure

class CompanyApi:

 # Инициализация
 """
				Инициализация класса CompanyApi.
               :param url: URL для доступа к API.

 """
 def __init__(self, url: str)-> None:
    self.url = url

# Получение токена
 @allure.step("api.Получить токен авторизации")
 def get_token(self, user: str = 'bloom', password: str = 'fire-fairy') -> str:
    """
				:param user: Имя пользователя для авторизации, по умолчанию 'bloom'.
                :param password: Пароль для авторизации, по умолчанию 'fire-fairy'.
                :return: Токен пользователя, полученный после авторизации.
                         Ответ от API в формате JSON.

    """
    creds = {
    "username": user,
    "password": password
        }
    resp = requests.post(self.url + '/auth/login', json=creds)
    return resp.json()["userToken"]


# Добавление компании:
 def create_company(self, name: str, description: str = "") -> dict:
     """
				Создание новой компании.
                :param name: Название компании.
                :param description: Описание компании, по умолчанию пустая строка.
                :return: Ответ от API в формате JSON.

      """
     company = {
    "name": name,
    "description": description
        }
     my_headers = {}
     my_headers["x-client-token"] = self.get_token()
     resp = requests.post(self.url + '/company',
     json=company, headers=my_headers)
     return resp.json()

#Удаление компании и сотрудников
 def delete_company(self, id: int) -> dict:
        """
				Удаление компании по её идентификатору.
                param id: Идентификатор компании для удаления.
                :return: Ответ от API в формате JSON.
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.get(self.url + '/company/delete/' + str(id), headers=my_headers)
        return resp.json()