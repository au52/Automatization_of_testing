class User:

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getFullName(self):
        return str(self.first_name) + ' ' + str(self.last_name)

#user= User('Ivan', 'Petrov')
#print(user.getFirstName())
#print(user.getLastName())
#print(user.getFullName())