'''

Пропущенные комменты 🌶️

При написании собственных функций рекомендуется в комментарии описывать назначение функции, ее параметры и возвращаемое значение. Часто программисты откладывают написание таких комментариев напоследок, а потом и вовсе забывают о них 😂.

На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python. Напишите программу, выводящую на экран имена всех функций, для которых отсутствует поясняющий комментарий. Будем считать, что любая строка, начинающаяся со слова def и пробела, является началом определения функции. Функция содержит комментарий, если первый символ предыдущей строки - #.

Формат входных данных
На вход программе подается строка текста, содержащая имя существующего текстового файла с кодом на языке Python.

Формат выходных данных
Программа должна вывести названия всех функций (не меняя порядка их следования в исходном файле), каждое на отдельной строке, для которых отсутствует поясняющий комментарий. Если все функции в файле имеют поясняющий комментарий, то следует вывести: Best Programming Team.

Примечание 1. Если бы файл содержал код:

def powers(a):
    return a, a**2, a**3

# функция вычисляет сумму всех переданных чисел
def sum_all(*args):
    return sum(args)

def matrix():
    pass

# функция возвращает количество переданных аргументов
def count_args(*args):
    return len(args)

def mean(*args):
    total = 0.0
    count = 0  
    for i in args:
        if type(i) in (int, float):
            total += i
            count += 1
    if count == 0:
        return 0.0
    else:
        return total / count
    
def greet(name, *args):
    args = (name,) + args
    return f'Hello, {" and ".join(args)}!'

# функция вычисляет факториал переданного числа
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

то результатом будет:

powers
matrix
mean
greet

Примечание 2. Гарантируется, что в файле есть хотя бы одна функция при этом вложенных функций в файле нет. 

'''
from time import sleep
check_lst=[False,False]
pretty_def=[]
all_def=[]
best_team = 'Best Programming Team' # Если совпадений не найдено
# должно соблюдаться условие: # и def, причем назад скакать не можем
with open('python_file.txt', 'r', encoding='UTF-8') as input_file:
    for line in input_file:
        check_lst[1]=[False, True][line.startswith('def')]
        if check_lst[0] and check_lst[1]:
            # temp = line.rstrip(':\n').replace('def ','').split('(')
            pretty_def+=[line.rstrip(':\n').replace('def ','').split('(')[0]]
        check_lst[0]=[False, True][line.startswith('#')]
        if line.startswith('def'):
            all_def+=[line.rstrip(':\n').replace('def ','').split('(')[0]]
        # print(check_lst)
        # sleep(1)
        # if check_lst[0] and check_lst[1]:
mset= set(all_def) - set(pretty_def)
if len(mset)>0:
    for i in all_def:
        if i in mset:
            print(i)
else:
    print(best_team)

file_name = input()
prev_str = ''
def_names = []

# with open(file_name, 'r') as input_file:
#     for line in input_file:
#         if line.startswith('def'):
#             if prev_str != '#':
#                 def_names.append(line[len('def '):line.find('(')])
#         else:
#             prev_str = line[0]

# if def_names:
#     print(*def_names, sep='\n')
# else:
#     print('Best Programming Team')


# with open(input(), encoding='utf-8') as code:
#     not_comm, preline = [], '_'
    
#     for l in code:
#         if l.startswith('def ') and preline[0] != '#':
#             not_comm += [l[4:l.find('(')]]
#         preline = l
            
#     print(*not_comm, sep='\n') if not_comm else print('Best Programming Team')
