'''
Города

Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур, 
однако к концу игры ввиду своего возраста забывают, какие города уже называли.

Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.

Формат входных данных
На вход программе в первой строке подаётся натуральное число n - количество названных городов, 
в последующих n строках вводятся названные города и ещё одна строка c новым, только что названым городом.

Формат выходных данных
Программа должна вывести OK, если этот город ещё не вспоминали, и REPEAT, если город уже был назван.
'''
city_quantity = int(input())
cities_list = [input() for _ in range (city_quantity+1)]
print(('OK','REPEAT')[len(cities_list)>len(set(cities_list))])