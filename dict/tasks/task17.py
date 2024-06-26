'''

Страны и города

На вход программе подается список стран и городов каждой страны. Затем даны названия городов. Напишите программу, которая для каждого города выводит, в какой стране он находится.

Формат входных данных
Программа получает на вход количество стран n. Далее идет nn строк, каждая строка начинается с названия страны, затем идут названия городов этой страны. В следующей строке записано число mm, далее идут mm запросов — названия каких-то mm городов, из перечисленных выше.

Формат выходных данных
Программа должна вывести название страны, в которой находится данный город в соответствии с примером.

Sample Input:

2
Германия Берлин Мюнхен Гамбург Дортмунд
Нидерланды Амстердам Гаага Роттердам Алкмар
4
Амстердам
Алкмар
Гамбург
Гаага

Sample Output:

Нидерланды
Нидерланды
Германия
Нидерланды
'''
res={}
#Словарь. Город ключ, страна значение

for _ in range(int(input())): #первый инпут
    lst = [i for i in input().split()]
    for i in range(1,len(lst)):
        res.update({lst[i]:lst[0]})
    
for _ in range(int(input())): #второй инпут
    city = input()
    print(res.get(city,''))

# d = {}
# for _ in range(int(input())):
#     country, *cities = input().split()
#     d.update(dict.fromkeys(cities, country))
# for _ in range(int(input())):    
#     print(d[input()])
