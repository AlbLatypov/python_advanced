# Хороший пароль

# Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, содержит хотя бы одну цифру, заглавную и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.

# Формат входных данных
# На вход программе подаётся одна строка текста.

# Формат выходных данных
# Программа должна вывести YES, если строка – хороший пароль, и NO в противном случае.
# Тестовые данные 🟢

# Sample Input 1:

# abcABC9

# Sample Output 1:

# YES

#Решение:
# - проверка 7 символов
# - 1 цифра, 1 заглавная, 1 строчная
# - any

import string

passw = input()

check = all([len(passw)>=7,\
             any(map(lambda x: x in string.ascii_lowercase, list(passw))), \
             any(map(lambda x: x in string.ascii_uppercase, list(passw))), \
             any(map(lambda x: x in string.digits, list(passw)))])
print(['YES','NO'][not check])
