import requests
import allure

class EmployeeApi:

# Инициализация
 def __init__(self, url: str):
    """
                  Инициализация класса EmployeeApi.
                  :param url: URL для доступа к API.

    """
    self.url = url

# Получение списка сотрудников
 def get_employee_list(self, params_to_add: dict) -> dict:
    """
                  Получение списка сотрудников.
                  :param params_to_add: Параметры для запроса.
                  :return: Список сотрудников в формате JSON.

    """
    resp = requests.get(self.url + '/employee', params=params_to_add)
    return resp.json()

# Получение токена
 @allure.step("api.Получить токен авторизации")
 def get_token(self, user: str = 'bloom', password: str = 'fire-fairy') -> str:
    """
                  Получение токена для авторизации.
                  :param user: Имя пользователя для авторизации, по умолчанию 'bloom'.
                  :param password: Пароль для авторизации, по умолчанию 'fire-fairy'.
                  :return: Токен пользователя, полученный после авторизации.

    """
    creds = {
    "username": user,
    "password": password
        }
    resp = requests.post(self.url + '/auth/login', json=creds)
    return resp.json()["userToken"]

# Добавление нового сотрудника
 def create_employee(self, f_Name: str, l_Name: str, id_com: int, phone: str, isActive: bool) -> dict:
        """
                  Добавление нового сотрудника.
                  :param f_Name: Имя сотрудника.
                  :param l_Name: Фамилия сотрудника.
                  :param id_com: Идентификатор компании.
                  :param phone: Номер телефона сотрудника.
                  :param isActive: Статус активности сотрудника.
                  :return: Ответ от API в формате JSON.

        """
        employee = {
            "firstName": f_Name,
            "lastName": l_Name,
            "companyId": id_com,
            "phone": phone,
            "isActive": isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', json=employee, headers=my_headers)
        return resp.json()

# Получение сотрудника по ID
 def get_employee(self, id: int) -> dict:
        """
                  Получение сотрудника по его идентификатору.
                  :param id: Идентификатор сотрудника.
                  :return: Информация о сотруднике в формате JSON.

        """
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()

# Изменение информации о сотруднике
 def edit_employee(self, new_id: int, new_mail: str, new_active: bool) -> dict:
    """
                  Изменение информации о сотруднике.
                  :param new_id: Идентификатор сотрудника для изменения.
                  :param new_mail: Новый адрес электронной почты.
                  :param new_active: Новый статус активности сотрудника.
                  :return: Ответ от API в формате JSON

    """
    my_headers = {}
    my_headers["x-client-token"] = self.get_token()
    employee = {
    "email": new_mail,
    "isActive": new_active
        }
    resp = requests.patch(self.url + '/employee/' +
    str(new_id), headers=my_headers, json=employee)
    return resp.json()