from Employee_class import Employee

main_url = 'https://x-clients-be.onrender.com'
employ = Employee(main_url)

# Проверки методов приложения x-clients
# -------------------
# 1. Получить токен авторизации
# 2. Добавить в список новую компанию
# 3. Проверить, что компания добавлена в список
# 4. Получить список сотрудников компании
# 5. Добавить нового сотрудника
# 6. Проверить, что сотрудник добавлен в список
# 7. Изменить информацию о сотруднике и проверить изменения
# 8. Удалить компанию


# 1. Получить токен авторизации
username = 'leonardo'
password = 'leads'
def test_get_token():
    global token
    token = employ.get_token(username, password)[0]
    token_get_status = employ.get_token(username, password)[1]
    assert token_get_status == 201

# 2. Добавить в список новую компанию
company_name = 'Счастливый бобёр'
company_description = 'Брёвна и пиломатериалы'
def test_add_new_company():
    global company_id
    company = employ.add_new_company(company_name, company_description, token)
    company_id = company[0]
    assert company[1] == 201

# 3. Проверить, что компания добавлена в список
def test_find_new_company():
    result = employ.find_company(company_id)
    assert result[1] == 200
    assert result[0]['name'] == company_name
    assert result[0]['description'] == company_description

# 4. Получить список сотрудников компании
def test_get_employees_list():
    employees_list = employ.get_employees_list(company_id)
    assert employees_list[1] == 200

firstName = "Олег"
lastName = "Попов"
# 5. Добавить нового сотрудника
def test_add_employee():
    result = employ.add_employee(company_id,firstName, lastName, token)
    global employ_id
    employ_id = result[0]['id']
    assert result[1] == 201

# 6. Проверить, что сотрудник добавлен в список
def test_get_employee():
    result = employ.get_employee(employ_id)
    assert result[1] == 200
    assert result[0]['firstName'] == 'Олег'
    assert result[0]['lastName'] == 'Попов'

email = "new_email@email.ru"
isActive = False
# 7. Изменить информацию о сотруднике и проверить изменения
def test_empoyee_change():
    employ_body_before = employ.get_employee(employ_id)[0]
    result = employ.empoyee_change(employ_id, email, isActive, token)
    employ_body_after = employ.get_employee(employ_id)[0]
    assert result[1] == 200
    assert employ_body_before['email'] != employ_body_after['email']
    assert employ_body_before['isActive'] != employ_body_after['isActive']

# 8. Удалить компанию
def test_delete_company():
    company_delete_status = employ.delete_company(company_id, token)
    assert company_delete_status == 200

