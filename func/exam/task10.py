# Напишите функцию compose(), которая принимает на вход две других одноаргументных функции f и g и возвращает новую функцию. Эта новая функция также должна принимать один аргумент x и применять к нему исходные функции в нужном порядке: для функций f и g порядок применения должен выглядеть, как f(g(x)).

# Примечание 1. Приведенный ниже код, при условии, что функция compose() написана правильно

# def add3(x):
#     return x + 3


# def mul7(x):
#     return x * 7


# print(compose(mul7, add3)(1))
# print(compose(add3, mul7)(2))
# print(compose(mul7, str)(3))
# print(compose(str, mul7)(5))

# должен выводить:

# 28
# 17
# 3333333
# 35

# Примечание 2. Вызывать функцию compose() не нужно, требуется только реализовать ее.

# Примечание 3. С точки зрения математики, композиция функций f и g — это новая функция h(x) = f(g(x)), при этом порядок применения функций f и g важен! 

def add3(x):
    return x + 3


def mul7(x):
    return x * 7

def compose(foo1, foo2):
    def tmp(x=1):
        return foo1(foo2(x))
    return tmp

print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))


# Офигенное решение 
# def compose(func, gunc):
#     return lambda x: func(gunc(x))
