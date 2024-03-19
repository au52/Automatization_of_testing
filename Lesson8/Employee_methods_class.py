import requests

class Employee():

    def __init__(self, url):
        self.url = url

# 1. Получить токен авторизации
    def get_token(self, user, pwd):
        auth_data = {
            "username": user,
            "password": pwd
        }
        resp = requests.post(self.url + '/auth/login', json=auth_data)
        return (resp.json()['userToken'], resp.status_code)

# 2. Создать новую компанию
    def add_new_company(self, name, description, token):
        company_data = {
            "name": name,
            "description": description
        }
        my_headers = {"x-client-token": token}
        resp = requests.post(self.url + '/company', json=company_data, headers=my_headers)
        return (resp.json()['id'], resp.status_code)

# 3. Проверить, что компания добавлена в список
    def find_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return (resp.json(), resp.status_code)

# 4. Получить список сотрудников компании
    def get_employees_list(self, id):
        resp = requests.get(self.url + '/employee', params={'company': str(id)})
        return (resp.json(), resp.status_code)

# 5. Добавить нового сотрудника
    def add_employee(self, id, firstName, lastName, token):
        data = {
            "id": 0,
            "firstName": firstName,
            "lastName": lastName,
            "middleName": "string",
            "companyId": id,
            "email": "email@email.ru",
            "url": "string",
            "phone": "string",
            "birthdate": "2024-03-16T07:14:53.833Z",
            "isActive": True
        }
        my_headers = {"x-client-token": token}
        resp = requests.post(self.url + '/employee', json=data, headers=my_headers)
        return (resp.json(), resp.status_code)

# 6. Запросить информацию о сотруднике
    def get_employee(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return (resp.json(), resp.status_code)

# 7. Изменить информацию о сотруднике
    def empoyee_change(self, id, email, isActive, token):
        data = {
            "lastName": "string",
            "email": email,
            "url": "string",
            "phone": "string",
            "isActive": isActive
        }
        my_headers = {"x-client-token": token}
        resp = requests.patch(self.url + '/employee/' + str(id), json=data, headers=my_headers)
        return (resp.json(), resp.status_code)

# 8. Удалить компанию
    def delete_company(self, id, token):
        my_headers = {"x-client-token": token}
        resp = requests.get(self.url + '/company/delete/' + str(id), headers=my_headers)
        return resp.status_code