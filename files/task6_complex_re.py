'''
Статистика по файлу

Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести три найденных числа в формате, приведенном в примере.

Примечание 1. Если бы файл file.txt содержал строки:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

то результатом было бы:

Input file contains:
108 letters 
20 words 
4 lines 

Примечание 2. Словом называется последовательность из непробельных символов. Например, строка

abc a21 67pop    qwert bo7ok 83456

содержит 6 слов: abc, a21, 67pop, qwert, bo7ok, 83456.
'''
import re
symbols=0
words=0
lines=0
with open('file.txt',encoding='utf-8') as file:
    lst=file.readlines()
    for i in lst:
        a=(re.sub(r'[^a-zA-Z\s]','',i).replace(' ','').replace('\n',''))
        words+= len(i.split())
        symbols+=len(a)
        lines+=1
print(f'Input file contains:\n{symbols} letters')
print(f'{words} words')
print(f'{lines} lines')
