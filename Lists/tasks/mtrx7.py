# На вход программе подаются два натуральных числа n и m. Напишите программу для создания матрицы размером n×m, заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.
import logging
logging.basicConfig(level = logging.DEBUG)

n,m = 3,4

lst = [[0]*m for _ in range(n)]
logging.debug(lst)

for i in range(n):
    for j in range(m):
        lst[i][j]='.' if (i+j) % 2 ==0 else '*'

for i in range(n):
    print(*lst[i])
