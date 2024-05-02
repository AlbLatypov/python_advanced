at=1
at2=1,2
at3=1,2,

print(type(at))
print(type(at2))
print(type(at3))

a, b, *tail = 1, 2, 3, 4, 5, 6
print(tail)

a, b, *tail, c = 1, 2, 3, 4, 5, 6
print(a,b,c, sep = ':')


info = ['timur', 'beegeek.org']
user, domain = info    # распаковка списка

print(user)
print(domain)

s1 = 'abc-de'.partition('-')
s2 = 'abc-de'.partition('.')
s3 = 'abc-de-fgh'.partition('-')

print(s1)
print(s2)
print(s3)
#Последовательно Фибоначи
a= 5
f1,f2=1,1
for i in range(a):
    print(f1)
    f1,f2 = f2,f1+f2

# Последовательность Трибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой трех предыдущих
# 1,1,1,3,5,9,17,31,57,105 …

print('Трибоначчи')
a= 10
list1=[1]*a
f1,f2,f3=1,1,1
for i in range(a):
    list1[i]=f1
    f1,f2,f3 = f2,f3,f3+f2+f1
print(*list1)

# tail всегда массив. Распаковать можно только один элемент
notes = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
do, re, mi, *tail = notes
print(tail)

tpl = (10, 20, 30, 40, 50, 60, 70, 80)
print(tpl[0:]) # начало среза начинается с 0
print(tpl[2:5]) # Если начинается с 0, то первым элементом будет 30, последний второй индекс клюевое это ДО НЕГО (НЕ ВКЛЮЧИТЕЛЬНО)
print(tpl[:4]) # До 4 элемента, не включительно = 0,1,2,3
print(tpl[3:]) # c 3 элемента включительно, до конца

tpl = (100, 200, 300, 400, 500)
print(tpl[-2]) # берем второй элемент с конца
print(tpl[-4:-1]) # с какого элемента? с -4, а это 200, по какой элемент количественно по -1, а это последний
