import requests
from employee import Employee


emp = Employee("https://x-clients-be.onrender.com")

#СОЗДАНИЕ НОВОГО СОТРУДНИКА
def test_add_new_employee():
    #Создание компании
    name = "DENIZ"
    description = "Компания по продаже товаров из Турции"
    result = emp.create_company(name, description)
    new_id = result["id"]

    #Создание нового сотрудника в компании
    f_Name = "Irem"
    l_Name = "Helvacioglu"
    id_com = new_id
    phone = "+79176172011"
    isActive = True
    new_emp = emp.create_employee(f_Name, l_Name, id_com, phone, isActive)
    newID = new_emp["id"]

#ПОЛУЧЕНИЕ СOТРУДНИКА ПО ID В СОЗДАННОЙ КОМПАНИИ (проверка, что сотрудник создан)
    new_employee = emp.get_employee(newID)
    
    assert new_employee["id"] == newID
    assert new_employee["firstName"] == f_Name
    assert new_employee["lastName"] == l_Name
    assert new_employee["isActive"] == True

   #Удаление созданной компании и сотрудников
    edited_company = emp.delete_company(new_id)
    assert edited_company["id"] == new_id
    assert edited_company["name"] == name
    assert edited_company["description"] == description
    assert edited_company["isActive"] == True

#ПОЛУЧЕНИЕ СПИСКА СОТРУДНИКОВ
def test_get_list_employee():
    #Создание компании
    name = "KPOPSHOP.RU"
    description = "Ваш K-POP магазин!"
    result = emp.create_company(name, description)
    new_id = result["id"]
    
    #Получение списка сотрудников компании(1)
    body = emp.get_employee_list(params_to_add={'company': new_id})
    len_before = len(body)

    #Создание сотрудника №1 в компании
    f_Name = "Park"
    l_Name = "Jimin"
    id_com = new_id
    phone = "+79197685544"
    isActive = True
    emp.create_employee(f_Name, l_Name, id_com, phone, isActive)

    #Создание сотрудника №2 в компании
    f_Name = "Jeon"
    l_Name = "Jungkook"
    id_com = new_id
    phone = "+79197685544"
    isActive = True
    emp.create_employee(f_Name, l_Name, id_com, phone, isActive)

    #Создание сотрудника №3 в компании
    f_Name = "Kim"
    l_Name = "Taehyung"
    id_com = new_id
    phone = "+79187775454"
    isActive = True
    emp.create_employee(f_Name, l_Name, id_com, phone, isActive)

    #Получение списка сотрудников компании(2)
    body_2 = emp.get_employee_list(params_to_add={'company': new_id})
    len_after = len(body_2)
 
    #Проверка, что созданные сотрудники появились в списке сотрудников компании
    assert len_after - len_before == 3

    #Удаление созданной компании и сотрудников
    edited_company = emp.delete_company(new_id)
    assert edited_company["id"] == new_id
    assert edited_company["name"] == name
    assert edited_company["description"] == description
    assert edited_company["isActive"] == True


#ИЗМЕНЕНИЕ ИНФОРМАЦИИ О СОТРУДНИКЕ
def test_edit_employee():
    #Создание компании
    name = "DIVYA"
    description = "Лучшие товары из Индии!"
    result = emp.create_company(name, description)
    new_id = result["id"]

    #Создание сотрудника в компании
    f_Name = "Khan"
    l_Name = "Shah Rukh"
    id_com = new_id
    phone = "+79156646743"
    isActive = True
    new_emp = emp.create_employee(f_Name, l_Name, id_com, phone, isActive)
    id_emp = new_emp["id"]

    #Изменение информации о сотруднике
    new_mail = "SRH@gmail.com"
    new_active = False
    edited = emp.edit(id_emp, new_mail, new_active)

    assert edited["id"] == id_emp

    #Проверка, что данные сотрудника изменились
    employee = emp.get_employee(id_emp)
    
    assert employee["email"] == new_mail
    assert employee["isActive"] == new_active 

    #Удаление созданной компании и сотрудников
    edited_company = emp.delete_company(new_id)
    assert edited_company["id"] == new_id
    assert edited_company["name"] == name
    assert edited_company["description"] == description
    assert edited_company["isActive"] == True
