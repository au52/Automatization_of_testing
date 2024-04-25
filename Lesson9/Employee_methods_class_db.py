from sqlalchemy import create_engine
from sqlalchemy.sql import text

class Employee_db():
#    Добавьте в тесты  методы работы с БД,
#    которые создают, удаляют, редактируют
#    и  вычитывают записи из БД.

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_company_list(self):
        return self.db.execute(text("select * from company")).fetchall()

    def get_company_by_id(self, id):
        return self.db.execute(text("select * from company where id = :select_id"), select_id = id).fetchall()

    def get_employees_list_by_company_id(self, id):
        return self.db.execute(text("select * from employee where company_id = :id"), id = id).fetchall()

    def add_new_emplpoyee(self, first_name, last_name, phone, company_id):
        self.db.execute(text("insert into employee (first_name, last_name, phone, company_id)"
                             " values (:first_name, :last_name, :phone, :company_id)"), first_name = first_name,
                        last_name = last_name, phone = phone, company_id = company_id)

    def max_employee_id(self):
        return self.db.execute(text("select MAX(id) from employee")).fetchall()[0][0]

    def get_employee_by_id(self, id):
        return self.db.execute(text("select * from employee where id = :id"), id = id).fetchall()

    def change_employee_data(self, id, new_fname, new_lname='string', new_status=True, new_phone='string', new_email='string'):
        self.db.execute(text("update employee set first_name = :first_name, last_name = :last_name, "
                                    "is_active = :is_active, phone = :phone, email = :email where id = :id"),
                               id=id, first_name = new_fname, last_name = new_lname, is_active = new_status,
                        phone = new_phone, email = new_email)

    def delete_employee_by_id(self, id):
        self.db.execute(text("delete from employee where id = :id"), id = id)

    def delete_company_by_id(self, id):
        self.db.execute(text("delete from company where id = :id"), id = id)


