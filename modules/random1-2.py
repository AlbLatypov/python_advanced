# Сгенерировать пароль из числа N символов [a-zA-Z]
import random
lst = []
length = int(input())    # длина пароля
for _ in range(length):
    lst += [chr([random.randint(65,90), random.randint(97,122)][random.randint(0,1)])]

print(*lst,sep='')


# Лотерейный билет. 7 разных чисел в диапазоне 1 -49 включительно.
import random
lst = []
while len(set(lst)) < 7:
    lst += [random.randint(1,49)]

print(*sorted(lst),sep=' ')
