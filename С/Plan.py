from typing import *
from Academic import *
from Practice import *


class Plan:
    def __init__(self, код_направления: str, название_направления: str, кафедра: str, список_основных_дисциплин: List[Academic],
                 список_практик: List[Practice]):
        self.код_направления = код_направления
        self.название_направления = название_направления
        self.кафедра = кафедра
        self.список_основных_дисциплин = список_основных_дисциплин
        self.список_практик = список_практик

    def __str__(self):
        def strr():
            s = '\n\nспикок основных дисциплин: \n\n---------------\n\n'
            for i in self.список_основных_дисциплин:
                s += str(i) + '\n'
            s += '---------------\n\n\n\nсписок практик: \n\n---------------\n\n'
            for i in self.список_практик:
                s += str(i) + "\n"
            s+='---------------'
            return s

        return f'код направления: {self.код_направления}\n' \
               f'название направления: {self.название_направления}\n' \
               f'кафедра: {self.кафедра}\n' \
               f'{strr()}'

    def __len__(self):
        return len(self.список_основных_дисциплин)

    def concatPract(self):
        return self.список_основных_дисциплин + self.список_практик

    def получить_дисциплину(self, i):
        return self.concatPract()[i]

    def изменить_дисциплину(self, index, newVal):
        self.concatPract()[index] = newVal

    def удалить_дисциплину(self, index):
        del self.concatPract()[index]


    def __add__(self, other):
        if type(other == Academic): self.список_основных_дисциплин.append(other)
        if type(other == Practice): self.список_практик.append(other)
        

    def writeFile(self):
        try:
            with open('result.txt', 'w', encoding='UTF-16') as file:
                file.write(str(self))
        except:
            print('Не удалось записать инофрмацию в файл')
