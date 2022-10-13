# Написать функцию tic_tac_toe(board), которая получает состояние поля для игры в крестики-нолики и опредляет победителя. 
# Поле представлено в виде спсика 3x3, где значение равно 0 - точка пуста, 1 - это «X», или 2 - это «O».
# Функция должна возвращать: -1 если это ничья.
#
# Пример:
# tic_tac_toe([[1, 1, 1],
#              [0, 2, 2],
#              [0, 0, 0]]) ==> 1


import traceback


def tic_tac_toe(board):
    def check(c):
        def g(n):
            return board[n // 3][n % 3]

        if g(c[0]) == g(c[1]) and g(c[1]) == g(c[2]): return g(c[0])
        return 0

    combs = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];

    for i in combs:
        if check(i): return check(i)

    for i in board:
        for i2 in i:
            if i2 == 0: return -1

    return 0

# Тесты
try:
    board1 = [[0, 0, 1],
              [0, 1, 2],
              [2, 1, 0]]
    assert tic_tac_toe(board1) == -1
    board2 = [[1, 1, 1],
              [0, 2, 2],
              [0, 0, 0]]
    assert tic_tac_toe(board2) == 1
    board3 = [[1, 2, 1],
              [1, 2, 2],
              [2, 2, 1]]
    assert tic_tac_toe(board3) == 2
    board4 = [[2, 1, 2],
              [2, 1, 1],
              [1, 2, 1]]
    assert tic_tac_toe(board4) == 0
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
