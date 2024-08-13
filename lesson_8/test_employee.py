import requests
from lesson_8.pages_employee.Employee import Employee
from lesson_8.pages_employee.Employee import Company

emp = Employee("https://x-clients-be.onrender.com")
com = Company("https://x-clients-be.onrender.com")

#СОЗДАНИЕ НОВОГО СОТРУДНИКА
def test_add_new_employee():
    #Создание компании
    name = "DENIZ"
    description = "Компания по продаже товаров из Турции"
    result = com.create_company(name, description)
    new_id = result["id"]

    #Создание нового сотрудника в компании
    f_Name = "Irem"
    l_Name = "Helvacioglu"
    phone = "+79176172011"
    isActive = True
    new_emp = emp.create_employee(f_Name, l_Name, new_id, phone, isActive)
    newID = new_emp["id"]

#ПОЛУЧЕНИЕ СOТРУДНИКА ПО ID В СОЗДАННОЙ КОМПАНИИ (проверка, что сотрудник создан)
    new_employee = emp.get_employee(newID)
    
    assert new_employee["id"] == newID
    assert new_employee["firstName"] == f_Name
    assert new_employee["lastName"] == l_Name
    assert new_employee["isActive"] == True

   #Удаление созданной компании и сотрудников
    edited_company = com.delete_company(new_id)
    assert edited_company["id"] == new_id
    assert edited_company["name"] == name
    assert edited_company["description"] == description
    assert edited_company["isActive"] == True

#ПОЛУЧЕНИЕ СПИСКА СОТРУДНИКОВ
def test_get_list_employee():
    #Создание компании
    name = "KPOPSHOP.RU"
    description = "Ваш K-POP магазин!"
    result = com.create_company(name, description)
    new_id = result["id"]
    
    #Получение списка сотрудников компании(1)
    body = emp.get_employee_list(params_to_add={'company': new_id})
    len_before = len(body)

    #Создание сотрудника №1 в компании
    f_Name = "Park"
    l_Name = "Jimin"
    phone = "+79197685544"
    isActive = True
    emp.create_employee(f_Name, l_Name, new_id, phone, isActive)

    #Создание сотрудника №2 в компании
    f_Name = "Jeon"
    l_Name = "Jungkook"
    phone = "+79197685544"
    isActive = True
    emp.create_employee(f_Name, l_Name, new_id, phone, isActive)

    #Создание сотрудника №3 в компании
    f_Name = "Kim"
    l_Name = "Taehyung"
    phone = "+79187775454"
    isActive = True
    emp.create_employee(f_Name, l_Name, new_id, phone, isActive)

    #Получение списка сотрудников компании(2)
    body_2 = emp.get_employee_list(params_to_add={'company': new_id})
    len_after = len(body_2)
 
    #Проверка, что созданные сотрудники появились в списке сотрудников компании
    assert len_after - len_before == 3

    #Удаление созданной компании и сотрудников
    edited_company = com.delete_company(new_id)
    assert edited_company["id"] == new_id
    assert edited_company["name"] == name
    assert edited_company["description"] == description
    assert edited_company["isActive"] == True


#ИЗМЕНЕНИЕ ИНФОРМАЦИИ О СОТРУДНИКЕ
def test_edit_employee():
    #Создание компании
    name = "DIVYA"
    description = "Лучшие товары из Индии!"
    result = com.create_company(name, description)
    new_id = result["id"]

    #Создание сотрудника в компании
    f_Name = "Khan"
    l_Name = "Shah Rukh"
    phone = "+79156646743"
    isActive = True
    new_emp = emp.create_employee(f_Name, l_Name, new_id, phone, isActive)
    id_emp = new_emp["id"]

    #Изменение информации о сотруднике
    new_mail = "SRH@gmail.com"
    new_active = False
    edited = emp.edit_employee(id_emp, new_mail, new_active)

    assert edited["id"] == id_emp

    #Проверка, что данные сотрудника изменились
    employee = emp.get_employee(id_emp)
    
    assert employee["email"] == new_mail
    assert employee["isActive"] == new_active 

    #Удаление созданной компании и сотрудников
    edited_company = com.delete_company(new_id)
    assert edited_company["id"] == new_id
    assert edited_company["name"] == name
    assert edited_company["description"] == description
    assert edited_company["isActive"] == True

