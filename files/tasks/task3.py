'''
Переворот строки

Вам доступен текстовый файл text.txt с одной строкой текста. Напишите программу, которая выводит на экран эту строку в обратном порядке.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести строку указанного файла в обратном порядке.
'''
with open('text.txt',encoding='utf-8') as file:
    print(file.readline()[::-1])


#Вам доступен текстовый файл data.txt, в котором записаны строки текста. Напишите программу, выводящую все строки данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.

with open('data.txt',encoding='utf-8') as file:
    lst=file.readlines()
    for i in range(len(lst)-1,-1,-1):
        print(lst[i].strip())

# Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все строки наибольшей длины из файла, не меняя их порядок.

with open('lines.txt',encoding='utf-8') as file:
    max1=max([len(i) for i in file.readlines()])
    print(max1)
    file.seek(0)
    lst=[i.strip() for i in file.readlines() if len(i)==19]
    print(*lst, sep='\n')
    # for i in file.readlines():
        


