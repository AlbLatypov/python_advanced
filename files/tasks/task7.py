'''
Random name and surname

Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия, а затем выводит их, каждую на отдельной строке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести текст в формате, приведенном в примере.

Примечание 1. Если бы файлы first_names.txt и last_names.txt содержали строки:

Aaron
Abdul
Abe
Abel
Abraham
Albert

и

Abramson
Adamson
Adderiy
Addington
Adrian
Albertson
Einstein

то результатом могло быть:

Abdul Albertson
Abel Adamson
Albert Einstein
'''
from random import choice as ch
with open('first_names.txt',encoding='utf-8') as fnames,open('last_names.txt',encoding='utf-8') as flast:
    lst_n=[i.rstrip('\n') for i in fnames.readlines()]
    last_l=[i.rstrip('\n') for i in flast.readlines()]
    for _ in range(3):
        print(f'{ch(lst_n)} {ch(last_l)}')


