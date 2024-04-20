from random import choice as ch

ffile='lines1.txt'

with open(ffile, encoding='utf-8') as f:
    temp = ch(f.readlines())
    print(temp.rstrip('\n'))


ffile='numbers1.txt'

with open(ffile, encoding='utf-8') as f:
    print(sum(map(int,f.readlines())))


ffile='nums1.txt'

with open(ffile, encoding='utf-8') as f:
    a=[i.strip() for i in f.readlines() if i.strip().isdigit()]
    print(sum(map(int,a)))


ffile='prices.txt'
result=0
with open(ffile, encoding='utf-8') as f:
    for el in f.readlines():
        a=el.replace('\n','').replace(' ','').split('\t')
        result+=int(a[1])*int(a[2])
print(result)

with open('da.txt', encoding='utf-8') as file:
    print('Repeat after me:', file.readline().strip())
    for line in file:
        print(line.strip() + '!')
