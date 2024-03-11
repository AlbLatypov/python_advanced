import sys
n = 5
list1=[[0]*n]*n
print(f'Исходный список = {list1},\nразмером {sys.getsizeof(list1)} байт')
for i in list1:
    print(f' Адрес в памяти элемента {i} = {id(i)}')
for j in range(n):
    list1[n-1][j] = j+1
for i in list1:
    print(f'{i}')
print(f'Результирующий список = {list1},\nразмером {sys.getsizeof(list1)} байт')