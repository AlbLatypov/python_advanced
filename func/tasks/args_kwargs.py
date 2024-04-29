# позиционные, аргс и кваргс
def test_foo (a,b, *args, **kwargs):
    print(a,b)
    print(args)
    print(kwargs)


# вывести количество аргументов
def count_args(*args):
    return (len(args))

#принимает произвольное количество числовых аргументов и возвращает сумму их квадратов.
def sq_sum(*args):
    args = [i*i for i in args]
    return sum(args)

# Напишите функцию mean(), которая принимает произвольное количество аргументов и возвращает среднее арифметическое 
# переданных в нее числовых (int или float) аргументов.
# Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.
# Примечание 2. Функция должна игнорировать аргументы всех типов, кроме int или float.
def mean(*args):
    if len(args) == 0:
        args = (0.0,)
    lst = [i for i in args if type(i) is int or type(i) is float]
    return (sum(lst) / len(lst) if len(lst) != 0 else float('0.0'))


test_foo(10, 12, 45, 200, 'loser', money=300, name='zoroo')
print('-------------------------------------')
print(count_args())
print(count_args(10))
print(count_args('stepik', 'beegeek'))
print(count_args([], (''), 'a', 12, False))
print('-------------------------------------')
print(sq_sum())
print(sq_sum(2))
print(sq_sum(1.5, 2.5))
print(sq_sum(1, 2, 3))
print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print('-------------------------------------')
print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(mean(False, True, 'gaga'))


