'''
Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера. При этом (в зависимости от переданных аргументов) она должна вести себя так:

    matrix() — возвращает матрицу 1×1, в которой единственное число равно нулю;
    matrix(n) — возвращает матрицу n × n, заполненную нулями;
    matrix(n, m) — возвращает матрицу из n строк и m столбцов, заполненную нулями;
    matrix(n, m, value) — возвращает матрицу из n строк и m столбцов, в которой каждый элемент равен числу value.

При создании функции пользуйтесь аргументами по умолчанию.

Примечание 1. Приведенный ниже код:

print(matrix())         # матрица 1 × 1 из 0
print(matrix(3))        # матрица 3 × 3 из 0
print(matrix(2, 5))     # матрица 2 × 5 из 0
print(matrix(3, 4, 9))  # матрица 3 × 4 из 9

должен выводить:

[[0]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
[[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]
'''

def matrix(n=1, m=None, value=0):
    # print(matrix.__defaults__)
    if m is None:
        m = n
    return [[value]*m for _ in range(n)]

print(matrix(3,4,9))

#пример ниже, как делать не стоит... Если значение по умолчанию изменяемый объект, то его изменение повлияет на каждый следующий вызов функции.

def append_foo (el, seq=[]):
    seq.append(el)
    return seq

print('Значение по умолчанию', append_foo.__defaults__)

print('Значение по умолчанию', append_foo.__defaults__)
print(append_foo(10))
print('Значение по умолчанию', append_foo.__defaults__)
print(append_foo(5))
print('Значение по умолчанию', append_foo.__defaults__)
print(append_foo(1))
print('Значение по умолчанию', append_foo.__defaults__)

# Решение в данном случае, использование None

def append_foo_1(element, seq=None):
    if seq is None:
        seq = []
    seq.append(element)
    return seq
