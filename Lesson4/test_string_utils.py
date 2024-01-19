from string_utils import StringUtils

su = StringUtils()

# Проверки метода capitilize

# def test_capitilize0():
#     res = su.capitilize('abcd')
#     assert res == 'Abcd'
#
# def test_capitilize1():
#     res = su.capitilize('Abcd')
#     assert res == 'Abcd'
#
# def test_capitilize2():
#     res = su.capitilize('1234')
#     assert res == '1234'
#
# def test_capitilize3():
#     res = su.capitilize('')
#     assert res == ''
#
# def test_capitilize4():
#     res = su.capitilize(' ')
#     assert res == ' '
#
# def test_capitilize5():
#     res = su.capitilize(' abcd')
#     assert res == ' abcd'
#
# def test_capitilize6():
#     res = su.capitilize('.:;! @*')
#     assert res == '.:;! @*'

# Проверка метода trim

# def test_trim0():
#     res = su.trim(' abcd')
#     assert res == 'abcd'
#
# def test_trim1():
#     res = su.trim('                abcd')
#     assert res == 'abcd'
#
# def test_trim2():
#     res = su.trim('abcd')
#     assert res == 'abcd'
#
# def test_trim3():
#     res = su.trim(' ')
#     assert res == ''
#
# def test_trim4():
#     res = su.trim('')
#     assert res == ''
#
# def test_trim5():
#     res = su.trim(' 1 2 3 ')
#     assert res == '1 2 3 '
#
# def test_trim6():
#     res = su.trim(' .1@4$')
#     assert res == '.1@4$'

# Проверки метода to_list

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


