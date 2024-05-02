'''

Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и оценка разделены пробелом). Оценка - целое число от 0 до 100 включительно.

Напишите программу для добавления 5 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в файл new_scores.txt.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем new_scores.txt в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.

Примечание 2. Если бы файл class_scores.txt содержал строки:

Washington 83
Adams 86
Kingsman 100
MacDonald 95
Thomson 98

то файл new_scores.txt имел бы вид:

Washington 88
Adams 91
Kingsman 100
MacDonald 100
Thomson 100

'''
with open('new_scores.txt',mode = 'w', encoding='utf-8') as file_out, open('class_scores.txt', mode = 'r', encoding='utf-8') as file_in:
    for v in file_in.readlines():
        fname,fval = v.rstrip('\n').split()
        if int(fval)<96:
            file_out.write(f'{fname} {int(fval)+5}\n')
        else:
            file_out.write(f'{fname} 100\n')

# with open('class_scores.txt', 'r') as input_file, open('new_scores.txt', 'w') as file:
#     for row in input_file.readlines():
#         name, val = row.split()
#         file.write(f'{name} {[100, int(val) + 5][(int(val) + 5) < 100 ]}\n')

    

