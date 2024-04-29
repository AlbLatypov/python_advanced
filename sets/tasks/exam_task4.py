'''
Книги на прочтение

Руслан получил в конце учебного года список литературы на лето. 
Теперь ему надо выяснить, какие книги из этого списка у него есть. 
У Руслана на компьютере в текстовом файле записаны все книги из его домашней библиотеки в случайном порядке.

Напишите программу, определяющую для каждой книги из списка на прочтение, есть она у Руслана или нет.

Формат входных данных
На вход программе в первой строке подается натуральное число m — количество книг в домашней библиотеке Руслана. 
Во второй строке записано натуральное число n —  количество книг в списке на лето. 
Далее идут m строк с названиями книг из домашней библиотеки и n строк названий из списка на лето.

Формат выходных данных
Программа должна вывести n строк, в каждой из которых написано слово YES, если книга найдена в библиотеке, и NO, если нет.

'''

arthur_home = input()
arthur_to_read = input()
lib_home = {input() for _ in range(int(arthur_home))}
lib_to_read = [input() for _ in range(int(arthur_to_read))]
for el in lib_to_read:
    if el in lib_home:
        print('YES')
    else:
        print('NO')

# m, n = int(input()), int(input())
# home_library = {input() for _ in range(m)}
# summer_list = [input() for _ in range(n)]                                      
# [(print('YES' if i in home_library else 'NO'))for i in summer_list]

# m = int(input())
# n = int(input())
# home = {input() for _ in range(m)}

# for _ in range(n):
#     print(('NO','YES')[input() in home])
