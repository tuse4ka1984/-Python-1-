import requests


class CompanyApi:

 # Инициализация
 def __init__(self, url):
    self.url = url

# Получение токена
 def get_token(self, user='bloom', password='fire-fairy'):
    creds = {
    "username": user,
    "password": password
        }
    resp = requests.post(self.url + '/auth/login', json=creds)
    return resp.json()["userToken"]


# Добавление компании:
 def create_company(self, name, description=""):
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
 def delete_company(self, id):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.get(self.url + '/company/delete/' + str(id), headers=my_headers)
        return resp.json()
