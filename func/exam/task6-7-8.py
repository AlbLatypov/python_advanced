# Дан список слов words. Допишите код после оператора распаковки (*), который оборачивает в двойные кавычки все элементы списка words, а затем печатает результат на одной строке через пробел.

# Примечание. Вспомните про встроенную функцию map() и анонимные функции lambda.


words = 'the world is mine take a look what you have started'.split()

tmp = list(map(lambda x: f'"{x}"',list(words)))
print(*tmp)


# Дан список целых чисел numbers. Допишите код после оператора распаковки (*), для удаления из списка всех чисел-палиндромов и печати результата на одной строке через пробел.

# Примечание. Вспомните про встроенную функцию filter() и анонимные функции lambda.

numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
tmp = list(filter(lambda x: str(x) != str(x)[::-1], numbers))
print(*tmp)


# Дан список numbers, состоящий из кортежей. Допишите пропущенную часть программы, чтобы список sorted_numbers был упорядочен по убыванию среднего арифметического элементов кортежей списка numbers.

# Примечание. Вспомните про анонимные функции lambda.

numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

sorted_numbers = sorted(numbers, reverse=True, key=lambda x:sum(x) / len(x))

print(sorted_numbers)
