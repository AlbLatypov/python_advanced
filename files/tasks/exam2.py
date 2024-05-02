'''

Tail of a File

На вход программе подается строка текста с именем текстового файла. Напишите программу, выводящую на экран последние 10 строк данного файла.

Формат входных данных
На вход программе подается строка текста с именем существующего текстового файла.

Формат выходных данных
Программа должна вывести последние 10 строк этого файла.

Примечание 1. Считайте, что исполняемая программа и файл находятся в одной папке.

Примечание 2. Если количество строк в файле меньше 10, необходимо вывести содержимое файла полностью.

Примечание 3. Если бы файл содержал строки:

there are many different holidays
on the first of january we
celebrate new year on the
seventh of january and the
twenty-fifth of december we
have christmas the twenty-third
of february is the day of the
defenders of the motherland
or the army day then comes
easter and radonitsa the
first of may is the labour
day the ninth of may is
victory day the third of july
is independence day then comes
the seventh of november the day
of the october revolution and so on

то результатом будет:

of february is the day of the
defenders of the motherland
or the army day then comes
easter and radonitsa the
first of may is the labour
day the ninth of may is
victory day the third of july
is independence day then comes
the seventh of november the day
of the october revolution and so on

Примечание 4. Подумайте над ситуацией, когда файл очень большой и нерационально считывать все его содержимое в память компьютера.

'''
lst=[]
# with open(input(),'r') as file:
with open('dd1.txt','r', encoding='UTF-8') as file:
    while True:
        a = file.readline()
        if not a:
            # file.seek(0)
            break
        else:
            if len(lst) < 10:
               lst+=[a.strip()]
            else:
                del lst[0]
                lst+=[a.strip()]
print(*lst,sep='\n')

# file_name = input()
# top_ten = []
# with open(file_name, 'r') as input_file:
#     for line in input_file:

#         if len(top_ten) > 9:
#             del top_ten[0]

#         top_ten.append(line.strip())

# print(*top_ten, sep='\n')
