primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 22, 44, 1)
print(f'Простой вывод кортежа {primes}')
print(f'Распаковка кортежа')
print(*primes)
#Хоть кортежи и неизменяемый тип данных и не содержит метода sort он может быть остортирован через метод sorted
# на выходе получаем список. Который также может быть преобразован в кортеж.
print(tuple(sorted(primes)))
#tuple can be string
string1 = ''.join(str(primes))
print(string1)

poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data=tuple(list(poet_data[0:-1])+['Москва'])
poet_data = poet_data[:-1]+('Москва',)
print(poet_data)