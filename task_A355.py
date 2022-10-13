# Некоторые люди достигая определенного возраста, в шутку празднуют только 20 или 21 день рождения, навсегда. 
# С некоторыми математическими навыками это вполне возможно - нужно только выбрать правильную систему счисления. 
# Написать функцию happy_birthday(age), которая возвращает систему счисления, 
# в которой данный возраст выглядит как 20 или 21.  
#  
# Пример
# happy_birthday(32) ==> 16 -> 32(_в_10) == 20(_в_16)
# happy_birthday(39) ==> 19 -> 39(_в_10) == 21(_в_19)


import traceback

def fastCheck(num, ss):
    return (num == ss*2) or (num == ss*2+1)


def happy_birthday(age):
    a=1
    while True:
        if(fastCheck(age, a)): return a
        a+=1


# Тесты
try:
    assert happy_birthday(32) == 16
    assert happy_birthday(39) == 19
    assert happy_birthday(65) == 32
    assert happy_birthday(83) == 41
    assert happy_birthday(22) == 11
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")