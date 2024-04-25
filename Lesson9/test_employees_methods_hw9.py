from Employee_methods_class_api import Employee_api
from Employee_methods_class_db import Employee_db

api = Employee_api('https://x-clients-be.onrender.com')
db = Employee_db("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-"
                  "cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")

# Проверки методов приложения x-clients
# -------------------
# 1. Получить токен авторизации
# 2. Добавить в список новую компанию
# 3. Проверить, что компания добавлена в список
# 4. Получить список сотрудников компании
# 5. Добавить нового сотрудника
# 6. Проверить, что сотрудник добавлен в список
# 7. Изменить информацию о сотруднике и проверить изменения
# 8. Удалить информацию о сотруднике
# 9. Удалить информацию о компании


# 1. Получить токен авторизации
username = 'leonardo'
password = 'leads'
def test_get_token():
    global token
    token = api.get_token(username, password)[0]
    token_get_status = api.get_token(username, password)[1]
    assert token_get_status == 201

# 2. Добавить в список новую компанию
company_name = 'Счастливый бобёр'
company_description = 'Брёвна и пиломатериалы'
def test_add_new_company():
    global company_id
    company = api.add_new_company(company_name, company_description, token)
    company_id = company[0]
    assert company[1] == 201

# 3. Проверить, что компания добавлена в список
def test_find_new_company():
    result = api.find_company(company_id)
    assert result[1] == 200
    assert result[0]['name'] == company_name
    assert result[0]['description'] == company_description
# Проверка через BD
    company_db = db.get_company_by_id(company_id)[0]
    assert company_db[3] == company_name
    assert company_db[4] == company_description

# 4. Получить список сотрудников компании
def test_get_employees_list():
    employees_list = api.get_employees_list(company_id)
    assert employees_list[1] == 200
    assert len(employees_list[0]) == 0
# Проверка через BD
    assert len(db.get_employees_list_by_company_id(company_id)) == 0

firstName = "Олег"
lastName = "Попов"
phone = '12345678'

# 5. Добавить нового сотрудника
def test_add_employee():
# Через BD
    db.add_new_emplpoyee(firstName, lastName, phone, company_id)
# Получить id нового сотрудника
    global employee_max_id
    employee_max_id = db.max_employee_id()

# 6. Проверить, что сотрудник добавлен в BD
def test_get_employee():
    result = api.get_employee(employee_max_id)
    assert result[1] == 200
    assert result[0]['firstName'] == 'Олег'
    assert result[0]['lastName'] == 'Попов'
# Проверки через BD
    employ_db = db.get_employee_by_id(employee_max_id)[0]
    assert employ_db[4] == firstName
    assert employ_db[5] == lastName
    assert employ_db[7] == phone

email = "new_email@email.ru"
status = False
new_first_name = 'Педро'
new_last_name = 'де Валуа'
new_status = True
new_phone = '911'
new_email = '1@1.ru'

# 7. Изменить информацию о сотруднике и проверить изменения
def test_empoyee_change():
    employ_body_before = api.get_employee(employee_max_id)[0]
    result = api.empoyee_change(employee_max_id, email, status, token)
    employ_body_after = api.get_employee(employee_max_id)[0]
    assert result[1] == 200
    assert employ_body_before['email'] != employ_body_after['email']
    assert employ_body_before['isActive'] != employ_body_after['isActive']
# Проверки через BD
    db.change_employee_data(employee_max_id, new_first_name, new_last_name, new_status, new_phone, new_email)
    new_employee_data = db.get_employee_by_id(employee_max_id)[0]
    assert new_employee_data[4] == new_first_name
    assert new_employee_data[5] == new_last_name
    assert new_employee_data[8] == new_email

# 8. Удалить информацию о сотруднике
def test_delete_employee():
     before = db.get_employees_list_by_company_id(company_id)
     db.delete_employee_by_id(employee_max_id)
     after = db.get_employees_list_by_company_id(company_id)
     assert len(before) - len(after) == 1

# 9. Удалить информацию о компании
def test_delete_company():
    before = db.get_company_list()
    db.delete_company_by_id(company_id)
    after = db.get_company_list()
    assert len(before) - len(after) == 1

