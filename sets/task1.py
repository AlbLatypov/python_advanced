'''
Формат входных данных
На вход программе подаются две строки текста, содержащие числа, отделенные символом пробела.

Формат выходных данных
Программа должна вывести количество чисел, содержащихся одновременно как в первой строке, так и во второй.
'''
a=set(input().split(' '))
b=set(input().split(' '))
# intersection & - одновременно принадлежат каждому множеству
print(len(a & b))