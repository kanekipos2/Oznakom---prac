# Написать функцию break_camel_case, которая разбивает слова написанные CamelCase,
# используя в качестве разделителя пробел
#
# Примеры:
# break_camel_case("BreakCamelCase") ==> "Break Camel Case"

import traceback


def break_camel_case(s):
    if sum(map(str.isupper, s)) < 2: return s;
    for i in range(1, len(s)):
        if s[i].isupper() and s[i-1] != ' ':
            s = s[:i]+' '+s[i:]
    return s


# Тесты
try:
    assert break_camel_case("BreakCamelCase") == "Break Camel Case"
    assert break_camel_case("helloWorld") ==  "helloWorld"
    assert break_camel_case("helloWorld BreakCamelCase") == "hello World Break Camel Case"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
