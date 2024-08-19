from sqlalchemy import create_engine
from sqlalchemy.sql import text


class EmployeeTable:
    scripts = {
        "select": "select * from employee",
        "delete by id": text("delete from employee where id =:id_to_delete"),
        "insert new": text("insert into employee(\"first_name\", \"last_name\", \"phone\", \"company_id\", \"is_active\") values (:f_name, :l_name, :phone, :comp_id, :active)"),
        "get max id": "select MAX(\"id\") from employee",
        "select by id": text("select * from employee where id =:select_id"),
        "select by company id": text("select * from employee where company_id =:select_id"),
        "delete by company id": text("delete from employee where company_id =:id_to_delete")
    }

# Инициализация
    def __init__(self, connection_string: str):
        """
                   Инициализация класса EmployeeTable.
                   :param connection_string: Строка подключения к базе данных.

        """
        self.db = create_engine(connection_string)

# Получение списка сотрудников
    def get_employee_list(self) -> list:
        """
                   Получение списка сотрудников из базы данных.
                   :return: Список всех сотрудников в виде объектов SQLAlchemy.

        """
        return self.db.execute(self.scripts["select"]).fetchall()
    
# Удаление сотрудника
    def delete_employee(self, id: int) -> None:
        """         
                    Удаление сотрудника по ID.
                    :param id: Идентификатор сотрудника для удаления.
                    :return: None.

        """
        self.db.execute(self.scripts["delete by id"], id_to_delete=id)

# Создание сотрудника
    def create_employee(self, first_name: str, last_name: str, company_id: int, phone: str, is_active: bool) -> None:
        """         
                    Создание нового сотрудника.
                    :param first_name: Имя сотрудника.
                    :param last_name: Фамилия сотрудника.
                    :param company_id: Идентификатор компании, с которой связан сотрудник.
                    :param phone: Номер телефона сотрудника.
                    :param is_active: Статус активности сотрудника.
                    :return: None.

        """
        self.db.execute(self.scripts["insert new"], f_name=first_name, l_name=last_name, phone=phone, comp_id=company_id, active=is_active)

# Получение максимального количества сотрудников
    def get_max_id_employee(self) -> int:
        """         
                   Получение максимального ID из таблицы сотрудников.
                   :return: Максимальный идентификатор сотрудника.

        """
        return self.db.execute(self.scripts["get max id"]).\
            fetchall()[0][0]

# Получение сотрудника по ID
    def get_employee_by_id(self, id: int) -> dict:
        """         
                  Получение сотрудника по его идентификатору.
                  :param id: Идентификатор сотрудника.
                  :return: И формация о сотруднике в формате JSON.

        """
        return self.db.execute(self.scripts["select by id"], select_id=id).\
            fetchone()

# Получение сотрудников по ID компании
    def get_employees_by_company_id(self, id: int) -> list:
        """         
                        
                   Получение списка сотрудников по идентификатору компании.
                   :param id: Идентификатор компании.
                   :return: Список сотрудников в формате JSON.

        """
        return self.db.execute(self.scripts["select by company id"], select_id=id).\
            fetchall()

# Удаление сотрудников по ID компании 
    def delete_employees_by_company_id(self, id: int) -> None:
        """         
                        
                  Удаление сотрудников по идентификатору компании.
                  :param id: Идентификатор компании.
                  :return: None.

        """
        self.db.execute(self.scripts["delete by company id"], id_to_delete=id)