'''
Даны оценки по математике трёх учеников в 10-балльной шкале. Напишите программу, которая выводит такие оценки, которые встречаются не более, чем у двух учеников.

Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).

Формат выходных данных
Программа должна вывести множество оценок в порядке возрастания на одной строке, разделенных пробелами, в соответствии с условием задачи.

Примечание. Оценка ученика находится в диапазоне от 00 до 10 включительно.

 Sample Input 1:

1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 10 2 10 2 6 7 10 10 6
1 4 6 9 8 7 0 9 0 9 8 10

Sample Output 1:

0 1 2 3 4 5 7 8 9 10
'''

#Решение
# Cимметрическая разность множеств – это множество, включающее все элементы исходных множеств, 
# не принадлежащие одновременно обоим исходным множествам. Для этой операции существует метод symmetric_difference().
a,b,c = [set(input().split(' ')) for _ in range(3)]
# print(sorted(a.symmetric_difference(b), key=int))
# print(sorted(b.symmetric_difference(c), key=int))
d=a.symmetric_difference(b)
d.update(b.symmetric_difference(c))
print(*sorted(d, key=int))

