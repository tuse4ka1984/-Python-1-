from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeeTable:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_employees(self,id):
        return self.db.execute(self.__scripts["select"],id_company=id).fetchall()    
    

    def get_employees(self, id_company):
        # Выполнение запросов с параметром id_company
        return self.db.execute(self.__scripts["select"], id_company=id_company).fetchall()
