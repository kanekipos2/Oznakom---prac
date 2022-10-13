# Задан список положительных чисел arr и положительное число k.
# Написать функцию int_diff, которая определяет сколько раз
# разница между двумя различными числами из списка равна k
#
# Пример:
# int_diff([2, 2, 7, 8, 12, 16, 27], 5) ==> 3 ([2, 7], [2, 7], [7, 12])


import traceback


def int_diff(arr, k):
    awns = 0
    for i in range(len(arr)):
        for i2 in range(i+1, len(arr)):
            if(abs(arr[i] - arr[i2]) == k): awns+=1
    return awns


# Тесты
try:
    assert int_diff([1, 1, 5, 6, 9, 16, 27], 4) == 3
    assert int_diff([1, 1, 3, 3], 2) == 4
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")