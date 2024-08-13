from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable

api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")

def test_get_employees():
    #Шаг1: получить список компаний через API:
    api_result = api.get_employee_list()

    #Шаг2: получить список компаний из БД:
    db_result = db.get_employees()

    #Шаг2: проверить, что списки равны
    assert len(api_result) == len(db_result)