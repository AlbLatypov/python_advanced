# Дополните приведенный код, используя индексацию кортежа, чтобы переменная last, содержала последний элемент кортежа countries
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
print(countries[-1])

# Дополните приведенный код, используя срезы, так чтобы он вывел первые 66 элементов кортежа primes.
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71) 
print(primes[0:6])

# Дополните приведенный код, используя срезы, так чтобы он вывел элементы кортежа countries кроме первых двух.
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[2:])

# Дополните приведенный код, используя срезы, чтобы он вывел все элементы кортежа countries, кроме последних трех.
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[:-3])

# Дополните приведенный код, используя срезы, чтобы он вывел все элементы кортежа countries, кроме двух последних и трех первых.
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[3:-2])

# Дополните приведенный код так, чтобы переменная number содержала количество элементов кортежа countries.
countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
number = len(countries)
print(number)

# Дополните приведенный код так, чтобы он вывел сумму минимального и максимального элементов кортежа numbers.
numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
print(min(numbers)+max(numbers))

# Дополните приведенный код так, чтобы переменная index содержала индекс элемента «Slovenia» в кортеже countries.
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
index = countries.index('Slovenia')
print(index)

# Дополните приведенный код так, чтобы переменная number, содержала количество вхождений «Spain» в кортеж countries.
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
number = countries.count('Spain')
print(number)

# Дополните приведенный код, используя операторы конкатенации (+) и умножения кортежа на число (*), чтобы он вывел кортеж:

#  (1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13).
numbers1 = (1, 2, 3)
numbers2 = (6,)
numbers3 = (7, 8, 9, 10, 11, 12, 13)

print(numbers1*2+numbers2*9+numbers3)
