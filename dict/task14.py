'''
Словарь программиста

Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык. Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из этого словаря.

Формат входных данных
В первой строке задано одно целое число nn — количество слов в словаре. В следующих nn строках записаны слова и их определения, разделенные двоеточием и символом пробела. В следующей строке записано целое число m — количество поисковых слов, чье определение нужно вывести. В следующих mm строках записаны сами слова, по одному на строке.

Формат выходных данных
Для каждого слова, независимо от регистра символов, если оно присутствует в словаре, необходимо вывести его определение. Если слова в словаре нет, программа должна вывести "Не найдено", без кавычек.

Input:
5
Змея: язык программирования Python
Баг: от англ. bug — жучок, клоп, ошибка в программе
Конфа: конференция
Костыль: код, который нужен, чтобы исправить несовершенство ранее написанного кода
Бета: бета-версия, приложение на стадии публичного тестирования
3
Змея
Жаба
костыль

Sample Output 1:

язык программирования Python
Не найдено
код, который нужен, чтобы исправить несовершенство ранее написанного кода
'''
dct={}
for i in range(int(input())): # количество элементов словаря
    lst = [i for i in input().split(': ')]
    dct.update({lst[0].lower():lst[1]})

for i in range(int(input())): # ввод цифры для определения количества поисковых слов
    print(dct.get(input().lower(),'Не найдено'))
