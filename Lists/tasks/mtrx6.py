# Поиск элементов в секторах матрицы. см. Docs а матрицах описан подход.
N = int(input())
lst = [list(map(int,input().split())) for i in range(N)]
quater_up=[]
quater_right=[]
quater_down=[]
quater_left=[]

for i in range(N):
    for j in range(N):
        quater_up+= [lst[i][j]] if (i<j and i<N-1-j) else ''
        quater_right+= [lst[i][j]] if (i<j and i>N-1-j) else ''
        quater_down+= [lst[i][j]] if (i>j and i>N-1-j) else ''
        quater_left+= [lst[i][j]] if (i>j and i<N-1-j) else ''

print(f'Верхняя четверть: {sum(quater_up)}\n'
      f'Правая четверь: {sum(quater_right)}\n'
      f'Нижняя четверть: {sum(quater_down)}\n'
      f'Левая четверть: {sum(quater_left)}')

