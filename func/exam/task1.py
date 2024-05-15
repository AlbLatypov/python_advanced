# Пример вывода. В данном случае передача аргументов верная, итерации по ключам.
def display(**kwargs):
    for i in kwargs:
        print(i, end=' ')

display(emp='Kelly', salary=9000) #<--------- emp salary

# Важно понимать, также посмотреть с *args
from functools import reduce
import operator

def flatten(data):
    return reduce(operator.concat, data, [])

result = flatten([[1, 2], [3, 4], [], [5]])

print(result) #<------------------[1, 2, 3, 4, 5]


