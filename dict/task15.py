'''
Анаграммы 1

Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.


Sample Input 1:

thing
night

Sample Output 1:

YES
'''
# нужны 2 словаря: ключ - буква, значение - количество вхождений буквы в слово.
result = 'YES'
st1=input()
st2=input()
st1 = {i:[st1.count(i)] for i in set(st1)}
st2 = {i:[st2.count(i)] for i in set(st2)}
for i in set(st1):
    if st1.get(i,'') != st2.get(i,''):
        result = 'NO'
        break
print(result)

#Решение следующей задачи, аналогичная в принципе
# import re
# pattern = '[ .,!?:;-]'

# result = 'YES'
# st1=re.sub(pattern, '',input().lower())
# st2=re.sub(pattern, '',input().lower())
# st1 = {i:[st1.count(i)] for i in set(st1)}
# st2 = {i:[st2.count(i)] for i in set(st2)}
# for i in set(st1):
#     if st1.get(i,'') != st2.get(i,''):
#         result = 'NO'
#         break
# print(result)
