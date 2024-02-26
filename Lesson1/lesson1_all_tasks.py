# Task 1

my_name = 'Artem Ukhanov'
print(my_name)

# Task 2

my_age = 52
my_age = 55
print(my_age)

#Task 3

user_name = input()
print('Привет, ' + user_name)

# Task 4

first_name = input()
last_name = input()
print('Вас зовут: ' + first_name + ' ' + last_name)

# Task 5 - не существует

# Task 6

def print_greeting():
    print('Привет, мир!')

print_greeting()

# Task 7

def func_0():
    print(0, end='')

def func_1():
    print(1, end='')

def func_2():
    print(2, end='')

def func_3():
    print(3, end='')

def func_4():
    print(4, end='')

def func_5():
    print(5, end='')

def func_6():
    print(6, end='')

def func_7():
    print(7, end='')

def func_8():
    print(8, end='')

def func_9():
    print(9, end='')

func_8()
func_8()
func_0()
func_0()
func_5()
func_5()
func_5()
func_3()
func_5()
func_3()
func_5()

print() # Чтобы дальше печаталось со следующей строки

# Task 8

numbers = [8,8,0,0,5,5,5,3,5,3,5]

def print_number(num):
    print(num, end='')

for i in range(11):
    print_number(numbers[i])

