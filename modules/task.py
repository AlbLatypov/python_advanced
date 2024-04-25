'''
Напишите программу, которая с помощью модуля random генерирует 100 случайных номеров лотерейных билетов и выводит их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:

    номер не может начинаться с нулей;
    номер лотерейного билета должен состоять из 7 цифр;
    все 100 лотерейных билетов должны быть различными.

'''





from string import octdigits as odgt
from random import sample
from time import sleep
result=[]
s=[]
while len(set(result)) < 100:
    while True:
        s=sample(odgt,7)
        if s[0] != '0':
            break
    # sleep(1)
    result+=[''.join(s)]
print(len(result))
sleep(2)
print(*result, sep='\n')


