from enum import Enum

from Discipline import *
from enums import *


class Academic(Discipline):
    def __init__(self, название: str, семестр: int, кафедра: str, преподаватель: str, форма_контроля: control_form, часы: dict):
        super().__init__(название, семестр, кафедра)
        self.преподаватель = преподаватель
        self.форма_контроля = форма_контроля
        self.часы = часы

    def изменить_преподавателя(self, преподаватель):
        self.преподаватель = преподаватель

    def изменить_форму_контроля(self, форма_контроля):
        try:
            self.форма_контроля = форма_контроля
        except:
            print('Неверный формат формы контроля')

    def форматированная_печать_занятий(self):
        s = ''
        for i in self.часы.items():
            s+=(f'{i[0]}: {i[1]}ч занятий\n')
        return s

    def __str__(self):
        return f'' \
               f'название: {self.название} \n' \
               f'семестр: {self.семестр}\n' \
               f'кафедра: {self.кафедра}\n' \
               f'преподаватель: {self.преподаватель}\n' \
               f'форма контроля: {self.форма_контроля.name}\n' \
               f'{self.форматированная_печать_занятий()}'

