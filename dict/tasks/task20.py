'''
Даны три списка student_ids, student_names, student_grades, содержащие информацию о студентах.

Дополните приведенный код, используя генератор, так чтобы получить список result, содержащий вложенные словари в соответствии с образцом: [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...].

Примечание 1. Для параллельной итерации по всем трем спискам одновременно можно использовать встроенную функцию zip().

Примечание 2. Выводить содержимое списка result не нужно.
'''
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013'] 
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy'] 
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

a= dict(zip(student_ids,(zip(student_names,student_grades))))
print(a)
result = [{i:{v[0]:v[1]}} for i,v in a.items()]
           
print(result)


# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

# result = [{x: {y: z}} for x, y, z in zip(student_ids, student_names, student_grades)]

# n = len(student_grades)
# result = [{student_ids[n]: {student_names[n]: student_grades[n]}} for n in range(n)]
