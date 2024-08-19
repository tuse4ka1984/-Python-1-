from sqlalchemy import create_engine
from sqlalchemy.sql import text


class CompanyTable:
    scripts = {
        "select": "select * from company where deleted_at is NULL",
        "delete by id": text("delete from company where id =:id_to_delete"),
        "insert new": text("insert into company(\"name\") values (:new_name)"),
        "get max id": "select MAX(\"id\") from company where deleted_at is null",
        "select by id": text("select * from company where id =:select_id and deleted_at is null")
    }

 # Инициализация
    def __init__(self, connection_string: str):
        """
                  Инициализация класса CompanyTable.
                  :param connection_string: Строка подключения к базе данных.
        """
        self.db = create_engine(connection_string)

 # Получение списка компаний
    def get_companies(self) -> list:
        """
                   Создание новой компании.
                   :param name: Название новой компании.
                   :return: Список всех компаний в виде объектов SQLAlchemy.
        
        """
        return self.db.execute(self.scripts["select"]).fetchall()

 # Создание компании
    def create_company(self, name):
        self.db.execute(self.scripts["insert new"], new_name = name)

 # Удаление компании
    def delete_company(self, id: int) -> None:
        """
                   Удаление компании по ID.
                   :param id: Идентификатор компании для удаления.
                   :return: None.
        
        """
        self.db.execute(self.scripts["delete by id"], id_to_delete = id)

 # Получение максимального количества компаний
    def get_max_id(self) -> int:
        """
                    Получение максимального ID из таблицы компаний.
                    :return: Максимальный идентификатор компании.
        
        """
        return self.db.execute(self.scripts["get max id"]).\
            fetchall()[0][0]
 
 # Получение компании по ID
    def get_company_by_id(self, id: int) -> list:
        """
                    Получение компании по её идентификатору.
                    :param id: Идентификатор компании.
                    :return: Список компаний (должен содержать только один элемент).
        """
        return self.db.execute(self.scripts["select by id"], select_id = id).fetchall()