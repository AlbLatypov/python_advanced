'''
Даны по 10-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок третьего ученика, 
которые не встречаются ни у первого, ни у второго ученика.

Формат входных данных
На вход программе подаются оценки трех учеников, разделенные символом пробела (оценки каждого ученика на отдельной строке).

Формат выходных данных
Программа должна вывести множество оценок в порядке убывания на одной строке, разделенных пробелами, в соответствии с условием задачи.

Примечание. Оценка ученика находится в диапазоне от 00 до 1010 включительно.

 Sample Input 1:

1 5 4 2 5 6 6 2 3 3 5 2
2 3 5 1 2 1 2 6 7 1 1 6
1 4 6 9 8 7 0 9 0 9 8 10

Sample Output 1:

10 9 8 0
'''

# Решение
a,b,c = [set(input().split(' ')) for _ in range(3)]
d,e = c - a, c - b
print(*sorted(d & e, reverse=True, key=int))
