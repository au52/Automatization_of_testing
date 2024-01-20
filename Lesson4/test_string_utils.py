from string_utils import StringUtils

su = StringUtils()

# Проверки метода capitilize
# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
# ==============================

def test_capitilize0():
    res = su.capitilize('abcd')
    assert res == 'Abcd'

def test_capitilize1():
    res = su.capitilize('Abcd')
    assert res == 'Abcd'

def test_capitilize2():
    res = su.capitilize('1234')
    assert res == '1234'

def test_capitilize3():
    res = su.capitilize('')
    assert res == ''

def test_capitilize4():
    res = su.capitilize(' ')
    assert res == ' '

def test_capitilize5():
    res = su.capitilize(' abcd')
    assert res == ' abcd'

def test_capitilize6():
    res = su.capitilize('.:;! @*')
    assert res == '.:;! @*'

# Багов нет, метод работает только если
# первый символ - буква.


# Проверка метода trim
# Принимает на вход текст и удаляет пробелы в начале, если они есть
# ==============================

def test_trim0():
    res = su.trim(' abcd')
    assert res == 'abcd'

def test_trim1():
    res = su.trim('                abcd')
    assert res == 'abcd'

def test_trim2():
    res = su.trim('abcd')
    assert res == 'abcd'

def test_trim3():
    res = su.trim(' ')
    assert res == ''

def test_trim4():
    res = su.trim('')
    assert res == ''

def test_trim5():
    res = su.trim(' 1 2 3 ')
    assert res == '1 2 3 '

def test_trim6():
    res = su.trim(' .1@4$')
    assert res == '.1@4$'

# Багов нет, удаляет произвольное кол-во пробелов в начале строки
# Пустые строки и строки без начальных пробелов не изменяет


# Проверки метода to_list
# Принимает на вход текст с разделителем и возвращает список строк
# ==============================

def test_to_list0():
    res = su.to_list('1:2:3:4', delimeter=':')
    assert res == ['1','2','3','4']

def test_to_list1():
    res = su.to_list('a b c d', delimeter=' ')
    assert res == ['a','b','c','d']

def test_to_list2():
    res = su.to_list('1 a 2 b 3 c 4 d', delimeter='')
    assert res == ['1a2b3c4d']

def test_to_list3():
    res = su.to_list('1a2b3c4d')
    assert res == ['1a2b3c4d']

def test_to_list4():
    res = su.to_list('')
    assert res == []

def test_to_list5():
    res = su.to_list(' ! ! ! ', '!')
    assert res == [' ', ' ', ' ', ' ']

def test_to_list6():
    res = su.to_list('   ')
    assert res == []

def test_to_list7():
    res = su.to_list('', '*')
    assert res == []

# Баг: нет проверки на пустую строку в качестве разделителя.


# Проверки метода contains
# Возвращает `True`, если строка содержит искомый символ и `False` - если нет
# ==============================

def test_contains0():
    res = su.contains('AbCdEf', 'C')
    assert res == True

def test_contains1():
    res = su.contains('AbCdEf', 'n')
    assert res == False

def test_contains2():
    res = su.contains('   ', ' ')
    assert res == True

def test_contains3():
    res = su.contains('', '')
    assert res == True

def test_contains4():
    res = su.contains('. !@ %', '@')
    assert res == True

def test_contains5():
    res = su.contains('1ab2 3c 4d', ' 3c')
    assert res == True

# Багов нет

# Проверки метода delete_symbol
# Удаляет все подстроки из переданной строки
# ==============================

def test_delete_symbol0():
    res = su.delete_symbol('a1b1c1', '1')
    assert res == 'abc'

def test_delete_symbol1():
    res = su.delete_symbol('a b c ', ' ')
    assert res == 'abc'

def test_delete_symbol2():
    res = su.delete_symbol('     ', ' ')
    assert res == ''

def test_delete_symbol3():
    res = su.delete_symbol('a1b1c1', 'r')
    assert res == 'a1b1c1'

def test_delete_symbol4():
    res = su.delete_symbol('', '')
    assert res == ''

def test_delete_symbol5():
    res = su.delete_symbol('', 'a')
    assert res == ''

# Багов нет

# Проверки метода starts_with
# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет
# ==============================

def test_starts_with0():
    res = su.starts_with('SkyPro', 'S')
    assert res == True

def test_starts_with1():
    res = su.starts_with('SkyPro', 'k')
    assert res == False

def test_starts_with2():
    res = su.starts_with(' SkyPro', ' ')
    assert res == True

def test_starts_with3():
    res = su.starts_with('123SkyPro', '123')
    assert res == True

def test_starts_with4():
    res = su.starts_with('SkyPro', 'SkyPro')
    assert res == True

def test_starts_with5():
    res = su.starts_with('SkyPro', '')
    assert res == True

def test_starts_with6():
    res = su.starts_with('', '')
    assert res == True

# Баг: работает не только с одиночным символом, но
# и с последовательностью символов

# Проверки метода end_with
# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет
# ==============================

def test_end_with0():
    res = su.end_with('SkyPro', 'o')
    assert res == True

def test_end_with1():
    res = su.end_with('SkyPro', 'k')
    assert res == False

def test_end_with2():
    res = su.end_with('SkyPro ', ' ')
    assert res == True

def test_end_with3():
    res = su.end_with('SkyPro123', '123')
    assert res == True

def test_end_with4():
    res = su.end_with('SkyPro', 'SkyPro')
    assert res == True

def test_end_with5():
    res = su.end_with('SkyPro', '')
    assert res == True

def test_end_with6():
    res = su.end_with('', '')
    assert res == True

# Баг: работает не только с одиночным символом, но
# и с последовательностью символов

# Проверки метода is_empty
# Возвращает `True`, если строка пустая и `False` - если нет
# ==============================

def test_is_empty0():
    res = su.is_empty('')
    assert res == True

def test_is_empty1():
    res = su.is_empty('Abc d1@')
    assert res == False

def test_is_empty2():
    res = su.is_empty('   ')
    assert res == False

def test_is_empty3():
    res = su.is_empty('12345')
    assert res == False

# Баг: некорректно работает со строкой из пробелов,
# возвращает True, хотя строка не пустая.

# Проверки метода list_to_string
# Преобразует список элементов в строку с указанным разделителем
# ==============================

def test_list_to_string0():
    res = su.list_to_string(['1', 'a', '2', 'b'])
    assert res == '1, a, 2, b'

def test_list_to_string1():
    res = su.list_to_string(['1', '2', '3', '4'], '*')
    assert res == '1*2*3*4'

def test_list_to_string2():
    res = su.list_to_string(['a', 'b', 'c', 'd'], ' ')
    assert res == 'a b c d'

def test_list_to_string3():
    res = su.list_to_string([])
    assert res == ''

def test_list_to_string4():
    res = su.list_to_string([], '-')
    assert res == ''

def test_list_to_string5():
    res = su.list_to_string(['', '', ''], '-')
    assert res == '--'

def test_list_to_string6():
    res = su.list_to_string(['a', 'b', 'c'], '')
    assert res == 'abc'

# Багов нет