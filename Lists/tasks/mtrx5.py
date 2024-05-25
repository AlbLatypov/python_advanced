# Поиск элементов в секторах матрицы. см. Docs а матрицах описан подход.
el = int(input())
lst = [list(map(int,input().split())) for i in range(el)]
res=[]
for i in range(el):
    for j in range(el):
        res += [lst[i][j]] if (i>=j and i<=el-1-j) or \
                              (i<=j and i>=el-1-j) else ''

print(max(res))

