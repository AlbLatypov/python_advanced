'''
Даны по 1010-балльной шкале оценки по информатике трех учеников. Напишите программу, выводящую множество оценок, которые есть и у первого, и у второго учеников, но которых нет у третьего ученика.

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

5 3 2
'''
m_list = [set(input().split(' ')) for _ in range(3)]
# a,b,c = [set(input().split(' ')) for _ in range(3)]
print(*sorted((m_list[0] & m_list[1])-m_list[2], reverse=True, key=int))
#fix: -map +key
