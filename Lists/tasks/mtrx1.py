#  Sample Input 1:

# 4
# 2
# и
# швец
# и
# жнец
# и
# на
# дуде
# игрец

# Sample Output 1:

# и швец
# и жнец
# и на
# дуде игрец

# и и и дуде
# швец жнец на игрец

a = int(input()) #4
b = int(input()) #2
lst = [[0]*b for _ in range(a)]
for i in range(a):
    for j in range(b):
        lst[i][j] = input()
print(*[' '.join(i) for i in lst], sep='\n')
print('')
list(map(print,*lst))
# print(list(v))
