import pytest
from string_utils import StringUtils

su = StringUtils()

# Проверки метода capitilize
# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
# ==============================

@pytest.mark.parametrize('inp, out', [('abcd','Abcd'),
('Abcd','Abcd'), ('1234','1234'), ('',''), (' ',' '),
(' abcd',' abcd'), ('.:;! @*','.:;! @*')])

def test_capitalize(inp, out):
    assert su.capitilize(inp) == out

# Багов нет, метод работает только если
# первый символ - буква.


# Проверка метода trim
# Принимает на вход текст и удаляет пробелы в начале, если они есть
# ==============================

@pytest.mark.parametrize('inp, out', [(' abcd','abcd'),
('                abcd','abcd'), ('abcd','abcd'), (' ',''),
('',''), (' 1 2 3 ','1 2 3 '), (' .1@4$','.1@4$')])
def test_trim(inp, out):
    assert su.trim(inp) == out

# Багов нет, удаляет произвольное кол-во пробелов в начале строки
# Пустые строки и строки без начальных пробелов не изменяет


# Проверки метода to_list
# Принимает на вход текст с разделителем и возвращает список строк
# ==============================

@pytest.mark.parametrize('inp, delimeter, out', [('1:2:3:4',':',['1','2','3','4']),
('a b c d',' ',['a','b','c','d']), ('1 a 2 b 3 c 4 d','',['1a2b3c4d']),
('1a2b3c4d',',',['1a2b3c4d']), ('',',',[]), (' ! ! ! ','!',[' ', ' ', ' ', ' ']),
('   ',',',[]), ('','*',[])])
def test_to_list(inp, delimeter, out):
    assert su.to_list(inp, delimeter) == out

# Баг: нет проверки на пустую строку в качестве разделителя.


# Проверки метода contains
# Возвращает `True`, если строка содержит искомый символ и `False` - если нет
# ==============================

@pytest.mark.parametrize('inp, sym, out', [('AbCdEf','C',True),
('AbCdEf','n',False), ('   ',' ',True), ('','',True),
('. !@ %','@',True), ('1ab2 3c 4d',' 3c',True)])
def test_contains(inp, sym, out):
    assert su.contains(inp, sym) == out

# Багов нет


# Проверки метода delete_symbol
# Удаляет все подстроки из переданной строки
# ==============================

@pytest.mark.parametrize('inp, sym, out', [('a1b1c1','1','abc'),
('a b c ',' ','abc'), ('     ',' ',''), ('a1b1c1','r','a1b1c1'),
('','',''), ('','a','')])

def test_delete_symbol(inp, sym, out):
    assert su.delete_symbol(inp, sym) == out

# Багов нет


# Проверки метода starts_with
# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет
# ==============================

@pytest.mark.parametrize('inp, sym, out', [('SkyPro','S',True),
('SkyPro','k',False), (' SkyPro',' ',True), ('123SkyPro','123',True),
('SkyPro','SkyPro',True), ('SkyPro','',True), ('','',True)])
def test_starts_with(inp, sym, out):
    assert su.starts_with(inp, sym) == out

# Баг: работает не только с одиночным символом, но
# и с последовательностью символов


# Проверки метода end_with
# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет
# ==============================

@pytest.mark.parametrize('inp, sym, out', [('SkyPro','o',True),
('SkyPro','k',False), ('SkyPro ',' ',True), ('SkyPro123','123',True),
('SkyPro','SkyPro',True), ('SkyPro','',True), ('','',True)])
def test_end_with(inp, sym, out):
    assert su.end_with(inp, sym) == out

# Баг: работает не только с одиночным символом, но
# и с последовательностью символов


# Проверки метода is_empty
# Возвращает `True`, если строка пустая и `False` - если нет
# ==============================

@pytest.mark.parametrize('inp, res', [('',True), ('Abc d1@',False),
('   ',False), ('12345',False)])
def test_is_empty(inp, res):
    assert su.is_empty(inp) == res

# Баг: некорректно работает со строкой из пробелов,
# возвращает True, хотя строка не пустая.


# Проверки метода list_to_string
# Преобразует список элементов в строку с указанным разделителем
# ==============================

@pytest.mark.parametrize('inp, joiner, out', [(['1', 'a', '2', 'b'],', ','1, a, 2, b' ),
(['1', '2', '3', '4'],'*','1*2*3*4'), (['a', 'b', 'c', 'd'],' ','a b c d'),
([],' ,',''), ([],'-',''), (['', '', ''],'-','--'), (['a', 'b', 'c'],'','abc')])
def test_list_to_string(inp, joiner, out):
    assert su.list_to_string(inp, joiner) == out

# Багов нет