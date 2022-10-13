"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""

import re

def symbCheck(s):
    s = ord(s)
    if(
        s == 32 or          # пробел
        97 <= s <= 122 or   # a-z
        65 <= s <= 90       # A-Z
    ):
        return True
    return False

def replaceAll(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def wiki_function():
    with open('wikiInput.txt') as file:
        arr = []
        for i in file.readlines():
            if(i): arr.append(i)

        clear_arr = []
        for i in arr:
            str = ''
            for i2 in i:
                if symbCheck(i2): str+=i2
            clear_arr.append(str)

        s = ' '.join(clear_arr)
        s = re.sub(' +', ' ', s)

        dct = {}
        for i in s.split(' '):
            try:
                dct[i] += 1
            except:
                dct[i] = 1

        dct = sorted(dct.items(), key=lambda item: item[1], reverse=True)
        tw = []
        for i in range(10):
            print(f"[{i+1}]: {dct[i][0]} {(15-len(dct[i][0])) * ' '} {' ' if i!=9 else ''} | {dct[i][1]}")
            tw.append(dct[i][0])

        arr = []
        for i in s.split(' '):
            if i in tw: arr.append('PYTHON')
            else: arr.append(i)

        s = ''
        t = 0
        for i in arr:
            if(t + len(i) > 100):
                s+='\n'
                t = 0
            s += i + ' '
            t += (len(i)+1)

        with open('result.txt', 'w') as wr:
            wr.write(s)



    return 1

# Вызов функции
wiki_function()