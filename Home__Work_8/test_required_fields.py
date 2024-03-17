import requests
from Employee_class_2 import Employee2

main_url = 'https://x-clients-be.onrender.com'
employ = Employee2(main_url)

# Проверки обязательности полей
# -----------------------------

# Подготовка тестов
resp_auth = employ.get_token('leonardo', 'leads')
token = resp_auth[0]
company = employ.add_new_company('Счастливый бобёр', 'Брёвна и пиломатериалы', token)
company_id = company[0]

# 1. Получить список сотрудников компании
# ---------------------------------------

# ID сомпании указан в запросе
# ПРОЙДЕН: Метод вернул ожидаемый статус ответа
def test_get_employees_list_with_id():
    employees_list = employ.get_employees_list(company_id)
    assert employees_list[1] == 200

# ID сомпании отсутствует в запросе
# ПРОЙДЕН: Метод вернул ошибку
def test_get_employees_list_no_id():
    employees_list = employ.get_employees_list(None)
    assert employees_list[1] != 200

# 2. Добавить нового сотрудника
# -----------------------------

# Это полный набор данных для запроса
all_data = {
    "id": 0,
    "firstName": "Иван",
    "lastName": "Петров",
    "middleName": "Е",
    "companyId": company_id,
    "email": "email@email.ru",
    "url": "https://yandex.ru",
    "phone": "+12345678901",
    "birthdate": "2001-07-23T07:14:53.833Z",
    "isActive": True
    }
# Все поля запроса заполнены
# ПРОЙДЕН: Метод вернул ожидаемый статус ответа
def test_add_employee_with_all_data():
    global employee_id
    result = employ.add_new_employee(all_data, token)
    employee_id = result[0]['id']
    assert result[1] == 201

# Все поля запроса заполнены, нет токена
# ПРОЙДЕН: Метод вернул ошибку
def test_add_employee_no_token():
    result = employ.add_new_employee(all_data, None)
    assert result[1] != 201

# Обязательное поле id не заполнено
# ПРОВАЛЕН: Метод должен вернуть ошибку, но этого не происходит
def test_add_employee_no_id():
    data = all_data.copy()
    data['id'] = None
    result = employ.add_new_employee(data, token)
    assert result[1] != 201

# Обязательное поле firstName не заполнено
# ПРОЙДЕН: Метод вернул ошибку
def test_add_employee_no_firstName():
    data = all_data.copy()
    data['firstName'] = None
    result = employ.add_new_employee(data, token)
    assert result[1] != 201

# Обязательное поле lastName не заполнено
# ПРОЙДЕН: Метод вернул ошибку
def test_add_employee_no_lastName():
    data = all_data.copy()
    data['lastName'] = None
    result = employ.add_new_employee(data, token)
    assert result[1] != 201

# Обязательное поле companyId не заполнено
# ПРОЙДЕН: Метод вернул ошибку
def test_add_employee_no_companyId():
    data = all_data.copy()
    data['companyId'] = None
    result = employ.add_new_employee(data, token)
    assert result[1] != 201

# Обязательное поле isActive не заполнено
# ПРОВАЛЕН: Метод должен вернуть ошибку, но этого не происходит
def test_add_employee_no_isActive():
    data = all_data.copy()
    data['isActive'] = None
    result = employ.add_new_employee(data, token)
    assert result[1] != 201

# 3. Получить сотрудника по id
# -----------------------------

# Обязательное полу id заполнено
# ПРОЙДЕН: Метод вернул ожидаемый статус ответа
def test_get_employee_with_id():
    result = employ.get_employee(employee_id)
    assert result[1] == 200

# Обязательное полу id не заполнено
# ПРОЙДЕН: Метод вернул ошибку
def test_get_employee_no_id():
    result = employ.get_employee(None)
    assert result[1] != 200

# 4. Изменить информацию о сотруднике
# -----------------------------------

all_data2 = {
            "lastName": "Иванов",
            "email": "new_email@email.com",
            "url": "https://google.com",
            "phone": "+70000000000",
            "isActive": False
        }
# Все данные в запросе присутствуют
# ПРОЙДЕН: Метод вернул ожидаемый статус ответа
def test_employee_change_with_all_data():
    result = employ.empoyee_change(employee_id, all_data, token)
    assert result[1] == 200

# Все данные в запросе присутствуют,
# проверка изменения данных сотрудника
# ПРОВАЛЕН: Не изменяется телефонный номер сотрудника
def test_employee_changes_applying():
    result = employ.empoyee_change(employee_id, all_data2, token)
    employee = employ.get_employee(employee_id)
    assert employee[0]['lastName'] == "Иванов"
    assert employee[0]['email'] == "new_email@email.com"
    assert employee[0]['avatar_url'] == "https://google.com"
    assert employee[0]['phone'] == "+70000000000"
    assert employee[0]['isActive'] == False

# Отсутствует id сотрудника
# ПРОЙДЕН: Метод вернул ошибку
def test_employee_changes_no_id():
    result = employ.empoyee_change(None, all_data2, token)
    assert result[1] != 200

# Отсутствует тело запроса
# ПРОВАЛЕН: Метод должен вернуть ошибку, но этого не происходит
def test_employee_changes_no_body():
    result = employ.empoyee_change(employee_id, None, token)
    assert result[1] != 200

# Отсутствует токен
# ПРОВАЛЕН: Метод должен вернуть ошибку, но этого не происходит
def test_employee_changes_no_token():
    result = employ.empoyee_change(employee_id, all_data2, None)
    assert result[1] != 200











# 8. Удалить компанию
company_delete_status = employ.delete_company(company_id, token)
assert company_delete_status == 200

