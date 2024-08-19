from from_lesson_9.pages.CompanyApi import CompanyApi
from from_lesson_9.pages.EmployeeApi import EmployeeApi
from from_lesson_9.pages.CompanyTable import CompanyTable
from from_lesson_9.pages.EmployeeTable import EmployeeTable
import allure


db_connection_string = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
api_url = "https://x-clients-be.onrender.com"
api_comp = CompanyApi(api_url)
api_emp = EmployeeApi(api_url)
db_comp = CompanyTable(db_connection_string)
db_emp = EmployeeTable(db_connection_string)


@allure.title("Тест добавления нового сотрудника")
@allure.description("Этот тест проверяет, что новый сотрудник добавляется успешно.")
@allure.feature("CREATE")
@allure.severity("CRITICAL")

def test_add_new_employee():
    with allure.step("Создать организацию"):
            with allure.step("Сгенерировать название"):   
                name = "Sen Çal Kapimi"
                db_comp.create_company(name)
                company_id = db_comp.get_max_id()

    with allure.step("Создать сотрудника"):
             with allure.step("Сгенерировать данные сотрудника"):
                f_Name = "Serkan"
                l_Name = "Bolat"
                id_com = company_id
                phone = "+79654563377"
                isActive = True

             with allure.step("Вызвать API-метод для создания"):
                new_emp = api_emp.create_employee(f_Name, l_Name, id_com, phone, isActive)
                id_emp = new_emp["id"]

             with allure.step("Проверить,что сотруднику присвоен ID"):
                assert id_emp is not None

             with allure.step("Получить созданного сотрудника пр ID"):   
                employee = db_emp.get_employee_by_id(id_emp)
                 
             with allure.step("Проверить, что сотрудник создан"):
                    assert employee is not None

             with allure.step("Проверить поля нового сотрудника. Корректно заполнены"):   
                    assert employee["first_name"] == f_Name
                    assert employee["last_name"] == l_Name
                    assert employee["company_id"] == id_com
                    assert employee["phone"] == phone
                    assert employee["is_active"] == isActive

    with allure.step("Удалить организацию и сотрудников из БД"):
            db_emp.delete_employee(id_emp)
            db_comp.delete_company(company_id)

@allure.title("Тест получения списка сотрудников")
@allure.description("Этот тест проверяет, что возвращается правильное количество сотрудников по компании.")
@allure.feature("READ")
@allure.severity("NORMAL")
def test_get_employee_list():

        with allure.step("Создать организацию"):
            with allure.step("Сгенерировать название"):
                name = "Güneşi Beklerken"
                db_comp.create_company(name)
                company_id = db_comp.get_max_id()

        with allure.step("Создать сотрудника"):
             
             with allure.step("Сгенерировать данные сотрудника"):
                f_Name = "Kerem"
                l_Name = "Bürsin"
                phone = "+79176548799"
                isActive = True

        with allure.step("Добавить сотрудника в БД"):
            db_emp.create_employee(f_Name, l_Name, company_id, phone, isActive)

        db_result = db_emp.get_employees_by_company_id(company_id)
        api_result = api_emp.get_employee_list(params_to_add={'company': company_id})

        with allure.step("Проверить,что списки из БД и API равны"):
            assert len(db_result) == len(api_result)

        with allure.step("Проверить, что список сотрудников = 2"):   
            assert len(api_result) == 2

        with allure.step("Удалить организацию и сотрудников из БД"):
            db_emp.delete_employees_by_company_id(company_id)
            db_comp.delete_company(company_id)

@allure.title("Тест получения информации о сотруднике по ID")
@allure.description("Этот тест проверяет, что информация о сотруднике возвращается правильно.")
@allure.feature("Управление сотрудниками")
@allure.severity("NORMAL")
def test_get_employee():
        with allure.step("Создать организацию"):
            name = "HERCAI"
            db_comp.create_company(name)
            company_id = db_comp.get_max_id()
        with allure.step("Создать сотрудника"):
             
             with allure.step("Сгенерировать данные сотрудника"):
                f_Name = "Miran"
                l_Name = "Aslanbey"
                id_com = company_id
                phone = "+79196325849"
                isActive = True

        with allure.step("Добавить сотрудника в БД"):
            db_emp.create_employee(f_Name, l_Name, id_com, phone, isActive)

        with allure.step("Получить максимальное количество сотрудников"):   
            id_emp = db_emp.get_max_id_employee()

        with allure.step("Получить сотрудника по ID"):
            employee = api_emp.get_employee(id_emp)

        with allure.step("Проверить поля сотрудника. Корректно заполнены"):
            assert employee["firstName"] == f_Name
            assert employee["lastName"] == l_Name
            assert employee["companyId"] == id_com
            assert employee["phone"] == phone
            assert employee["isActive"] == isActive

        with allure.step("Удалить организацию и сотрудников из БД"):
            db_emp.delete_employee(id_emp)
            db_comp.delete_company(company_id)

@allure.title("Тест редактирования информации о сотруднике")
@allure.description("Этот тест проверяет, что информация о сотруднике редактируется корректно.")
@allure.feature("Управление сотрудниками")
@allure.severity("NORMAL")
def test_edit_employee():
        with allure.step("Создать организацию"):
            name = "Muhteşem"
            db_comp.create_company(name)
            company_id = db_comp.get_max_id()
        with allure.step("Создать сотрудника"):
             
             with allure.step("Сгенерировать данные сотрудника"):
                f_Name = "Meryem"
                l_Name = "Uzerli"
                id_com = company_id
                phone = "+79185664488"
                isActive = True

        with allure.step("Добавить сотрудника в БД"):
            db_emp.create_employee(f_Name, l_Name, id_com, phone, isActive)

        with allure.step("Получить максимальное количество сотрудников"):
            id_emp = db_emp.get_max_id_employee()

        with allure.step("Отредактировать данные сотрудника"):
            new_email = "MF@gmail.com.ru"
            new_Active = False
            api_emp.edit_employee(id_emp, new_email, new_Active)

        with allure.step("Получить сотрудника по ID"):
            employee = db_emp.get_employee_by_id(id_emp)

        with allure.step("Проверить, что сотруднику присвоен ноывй ID"):
            assert employee is not None

        with allure.step("Проверить, что данные сотрудника изменились"):  
            assert employee["first_name"] == f_Name
            assert employee["last_name"] == l_Name
            assert employee["company_id"] == id_com
            assert employee["phone"] == phone
            assert employee["email"] == new_email
            assert employee["is_active"] == new_Active

        with allure.step("Удалить организацию и сотрудников из БД"):
            db_emp.delete_employee(id_emp)
            db_comp.delete_company(company_id)