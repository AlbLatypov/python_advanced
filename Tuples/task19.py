'''
Конкурсный отбор

Напишите программу, которая выводит список хорошистов и отличников в классе.

Формат входных данных
На вход программе подается натуральное число n, далее следует n строк с фамилией школьника и его оценкой на каждой из них.

Формат выходных данных
Программа должна вывести сначала все введённые строки с фамилиями и оценками учеников в том же порядке. 
Затем следует пустая строка, а затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке).

 Sample Input 2:

5
Круглов 4
Кузнецов 5
Федин 4
Тарасов 2
Словецкий 3

Sample Output 2:

Круглов 4
Кузнецов 5
Федин 4
Тарасов 2
Словецкий 3

Круглов 4
Кузнецов 5
Федин 4
'''
# Обработка данных в момент ввода данных. По завершении - распаковка.
n=int(input())
students,best_students = (),()
for i in range(n):
    entered_string=input().split(' ')
    students+=tuple(entered_string),
    print(*students[i])
    if int(students[i][1])>3:
        best_students+=tuple(entered_string),  
print()
for best in best_students:
    print(*best)

#Этот пример конечно читабельнее, но 3 раза по данным бегает.

# students = [tuple(input().split()) for _ in range(int(input()))]

# for student in students:
#     print(*student)
    
# print()

# for name, grade in students:
#     if int(grade) > 3:
#         print(name, grade)
