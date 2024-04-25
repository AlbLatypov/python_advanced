from random import randint as ri
result=[]
s=[]
while len(set(s))<25:
    s+=[ri(1,75)]
    # print(s)

print(len(set(s)))
s=list(set(s))
s[12]=0

for i in range(0,25,5):
    a=s[i:i+5]
    print(*a, sep=' ')

