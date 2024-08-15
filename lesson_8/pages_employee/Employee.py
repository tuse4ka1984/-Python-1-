import requests


class Employee:

# Инициализация
 def __init__(self, url):
    self.url = url

# Получение списка сотрудников  
 def get_employee_list(self, params_to_add):
    resp = requests.get(self.url + '/employee', params=params_to_add)
    return resp.json()

# Получение токена
 def get_token(self, user='bloom', password='fire-fairy'):
    creds = {
    "username": user,
    "password": password
        }
    resp = requests.post(self.url + '/auth/login', json=creds)
    return resp.json()["userToken"]

# Добавление нового сотрудника
 def create_employee(self, f_Name, l_Name, id_com, phone, isActive):
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
 
  #Получение списка сотрудников
 def get_employee_list(self, params_to_add):
        resp = requests.get(self.url + '/employee', params=params_to_add)
        return resp.json()

# Получение сотрудника по ID
 def get_employee(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()
 
# Изменение информации о сотруднике
 def edit_employee(self, new_id, new_mail, new_active):
    my_headers = {}
    my_headers["x-client-token"] = self.get_token()
    employee = {
    "email": new_mail,
    "isActive": new_active
        }
    resp = requests.patch(self.url + '/employee/' +
    str(new_id), headers=my_headers, json=employee)
    return resp.json()
 
 





