# Найти максимальный элемент ниже главной диагонали. Диагональ слева вверх, право низ.
lst = ([max(list(map(int,input().split()[:i+1]))) for i in range(int(input()))])
print(max(lst))
