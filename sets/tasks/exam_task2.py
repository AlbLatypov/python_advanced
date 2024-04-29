'''
На спутнике «Восход» установлен прибор для измерения солнечной активности. 
Каждую минуту он передаёт в обсерваторию по каналу связи положительное целое число — 
количество энергии солнечного излучения. Для правильного анализа результатов нет необходимости держать повторяющиеся данные, 
поэтому их нужно удалить. Напишите программу, которая выводит максимальное количество показаний спутника, при удалении которых 
результат будет правильно проанализирован.

Формат входных данных
На вход программе подаётся одна строка, содержащая числа - показания спутника «Восход». Числа указываются через пробел и не содержат ведущих нулей.

Формат выходных данных
Программа должна вывести максимальное количество показаний, после удаления которых анализ результатов будет произведен верно.

Примечание. Рассмотрим 1 тест: у нас подаются данные 10 20 30 10 40 10. Мы видим, что число 10 содержится тут 3 раза – значит, 
повторяющиеся числа 10 надо удалить. Таких у нас 2 (первое число 10 мы не учитываем). Другие числа не повторяются, поэтому ответ будет 2.
'''
#Решение: из длины списка вычесть длину множества??? Условие выглядит страшнее, чем решение.
values=input()
values_list=values.split(' ')
print(len(values_list) - len(set(values_list)))