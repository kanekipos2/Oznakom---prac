# Написать функцию blocks, которая получает строку, состоящую из букв и цифр и возвращает строку в виде блоков,
# разделенных символом дефис. Элементы блока должны быть отсортированы по принципу, указанному ниже, и
# каждый блок не может содержать несколько экземпляров одного и того же символа.
# Порядок блоков:
# строчные буквы (a - z) в алфавитном порядке
# заглавные буквы (A - Z) в алфавитном порядке
# цифры (0 - 9) в порядке возрастания
#
#
# Примеры:
# blocks("21AxBz") ==> "xzAB12"
# blocks("abacad") ==> "abcd-a-a"

import traceback

def sFunc(n):
    if n.isdigit(): return 30 * ord(n)
    if n.isupper(): return 10 * ord(n)
    return ord(n)


def blocks(s):
    s = sorted(s, key=sFunc)
    cur_block = []
    ost = []
    for i in s:
        if i not in cur_block: cur_block.append(i)
        else: ost.append(i)
    return f"{''.join(cur_block)}-{blocks(''.join(ost))}" if ost else ''.join(cur_block)

# Тесты
try:
    assert blocks("21AxBz") == "xzAB12"
    assert blocks("abacad") == "abcd-a-a"
    assert blocks("heyitssampletestkk") == "aehiklmpsty-ekst-est"
    assert blocks("6zjX9qcwTIuYNvdmL3CtElHa2n0rogKsSVPRWG4QAMUOe8JkyfxZDiBpb1Fh75GUTLMcbio7HO6rvn1NtDRmPJAejuXVFgaZI3pK90s4fBzqwEd5yWCQh8Sl2kxY") == \
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
