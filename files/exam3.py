'''
Forbidden words 🌶️

На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран содержимое этого файла, но с заменой всех запрещенных слов звездочками * (количество звездочек равно количеству букв в слове).

Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Гарантируется, что все слова в этом файле записаны в нижнем регистре.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла, в котором необходимо заменить запрещенные слова звездочками.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание 1. Ваша программа должна заменить запрещенные слова, где бы они ни встречались, даже если они встречаются в середине другого слова.

Примечание 2. Программа должна заменять запрещенные слова независимо от их регистра. Например, если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и подобные должны быть заменены на ****.

Примечание 3. Если бы файл forbidden_words.txt содержал слова:

hello email python the exam wor is

а файл в котором заменяются слова имел бы вид:

Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!

то результатом будет:

*****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!
'''
# from time import sleep
# forb_filename = 'forbidden_words.txt'
# input_filename = 'data.txt'
# result_lst=[]
# with open(forb_filename, 'r') as file, open(input_filename,'r') as input_file:
#     f_words = file.read().split()
#     input_wors = input_file.read().split()
#     print(f_words)
#     print(input_wors)
#     for i in input_wors:
#         result_s=i
#         for z in range(1,len(i)+1):
#             check_slice = i[:z].lower()
#             if check_slice in f_words:
#                 result_s+=i.lower().replace(check_slice,'*'*len(check_slice))
#                 print(f'Исходное слово: {i} обработано')
#                 print(f'Срез: {check_slice}')
#                 print(f'После обработки: {result_s}')
#                 print(f'--------------------')
#                 # input()
#             # print(f'Слово {i} обрабатывать не нужно')
#             # result_s=i
#             # break
#         print('список')
#         result_lst+=[result_s]   
# print(*result_lst)        
file_name = input()
forbidden_words = {}
with open('forbidden_words.txt', 'r') as fw_file:
    forbidden_words = {word for word in fw_file.read().split()}
with open(file_name, 'r') as input_file:
    for line in input_file:
        low_line = line.lower()
        for key in forbidden_words:
            while key in low_line:
                low_line = low_line.replace(key, '*' * len(key))

        enc_line = ['*' if low_line[i] == '*' else line[i] for i in range(len(low_line))]
        print(''.join(enc_line), end='')

