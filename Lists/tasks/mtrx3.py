# Найти все элементы значение которых больше среднего ариф. в ряду.
elements = int(input())
lst = [list(map(int,input().split())) for i in range(elements)]
for el in lst:
    print(len(list(filter(lambda x: x>(sum(el)/elements),el))))
