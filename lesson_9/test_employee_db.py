from pages.CompanyApi import CompanyApi
from pages.EmployeeApi import EmployeeApi
from pages.CompanyTable import CompanyTable
from pages.EmployeeTable import EmployeeTable


db_connection_string = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
api_url = "https://x-clients-be.onrender.com"
api_comp = CompanyApi(api_url)
api_emp = EmployeeApi(api_url)
db_comp = CompanyTable(db_connection_string)
db_emp = EmployeeTable(db_connection_string)


def test_add_new_employee():
    name = "Sen Çal Kapimi"
    db_comp.create_company(name)
    company_id = db_comp.get_max_id()

    f_Name = "Serkan"
    l_Name = "Bolat"
    id_com = company_id
    phone = "+79654563377"
    isActive = True
    new_emp = api_emp.create_employee(f_Name, l_Name, id_com, phone, isActive)
    id_emp = new_emp["id"]

    assert id_emp is not None
    employee = db_emp.get_employee_by_id(id_emp)

    assert employee is not None
    assert employee["first_name"] == f_Name
    assert employee["last_name"] == l_Name
    assert employee["company_id"] == id_com
    assert employee["phone"] == phone
    assert employee["is_active"] == isActive

    db_emp.delete_employee(id_emp)
    db_comp.delete_company(company_id)


def test_get_employee_list():
    name = "Güneşi Beklerken"
    db_comp.create_company(name)
    company_id = db_comp.get_max_id()

    f_Name = "Kerem"
    l_Name = "Bürsin"
    phone = "+79176548799"
    isActive = True
    db_emp.create_employee(f_Name, l_Name, company_id, phone, isActive)
    db_emp.create_employee(f_Name, l_Name, company_id, phone, isActive)

    db_result = db_emp.get_employees_by_company_id(company_id)
    api_result = api_emp.get_employee_list(params_to_add={'company': company_id})

    assert len(db_result) == len(api_result)
    assert len(api_result) == 2

    db_emp.delete_employees_by_company_id(company_id)
    db_comp.delete_company(company_id)


def test_get_employee():
    name = "HERCAI"
    db_comp.create_company(name)
    company_id = db_comp.get_max_id()

    f_Name = "Miran"
    l_Name = "Aslanbey"
    id_com = company_id
    phone = "+79196325849"
    isActive = True
    db_emp.create_employee(f_Name, l_Name, id_com, phone, isActive)
    id_emp = db_emp.get_max_id_employee()

    employee = api_emp.get_employee(id_emp)

    assert employee["firstName"] == f_Name
    assert employee["lastName"] == l_Name
    assert employee["companyId"] == id_com
    assert employee["phone"] == phone
    assert employee["isActive"] == isActive

    db_emp.delete_employee(id_emp)
    db_comp.delete_company(company_id)


def test_edit_employee():
    name = "Muhteşem"
    db_comp.create_company(name)
    company_id = db_comp.get_max_id()

    f_Name = "Meryem"
    l_Name = "Uzerli"
    id_com = company_id
    phone = "+79185664488"
    isActive = True
    db_emp.create_employee(f_Name, l_Name, id_com, phone, isActive)
    id_emp = db_emp.get_max_id_employee()

    new_email = "MF@gmail.com.ru"
    new_Active = False
    api_emp.edit_employee(id_emp, new_email, new_Active)

    employee = db_emp.get_employee_by_id(id_emp)

    assert employee is not None
    assert employee["first_name"] == f_Name
    assert employee["last_name"] == l_Name
    assert employee["company_id"] == id_com
    assert employee["phone"] == phone
    assert employee["email"] == new_email
    assert employee["is_active"] == new_Active

    db_emp.delete_employee(id_emp)
    db_comp.delete_company(company_id)