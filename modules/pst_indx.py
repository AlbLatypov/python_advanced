'''
Почтовый индекс в Латверии имеет вид: 

LetterLetterNumber_NumberLetterLetter

где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

Примечание 1. Пример правильного (неправильного) индекса Латверии:

AB23_56VG          # правильный
V3F_231GT          # неправильный

Примечание 2. Обратите внимание на символ _ в почтовом индексе.

Примечание 3. Вызывать функцию generate_index() не нужно, требуется только реализовать.
'''
# import string
# from random import randrange as rr
# ltr=string.ascii_uppercase
# print(f'{ltr[rr(len(ltr))]}{ltr[rr(len(ltr))]}{rr(100)}_{rr(100)}{ltr[rr(len(ltr))]}{ltr[rr(len(ltr))]}')



# from random import choice, randint
# from string import ascii_uppercase as letter

# def generate_index():
#     return f'{choice(letter)}{choice(letter)}{randint(0, 99)}_{randint(0, 99)}{choice(letter)}{choice(letter)}'

from random import shuffle as sh
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

for i in range(len(matrix)):
    print(matrix[i])
    sh(matrix[i])

print(matrix)
