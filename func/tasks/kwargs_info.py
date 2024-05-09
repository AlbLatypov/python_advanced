# Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает именованные аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>, при этом имена аргументов следуют в алфавитном порядке (по возрастанию).

# Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество именованных аргументов.

# Примечание 2. Следующий программный код:

# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 

# должен выводить:

# age: 28
# first_name: Timur
# job: teacher
# last_name: Guev

def info_kwargs(**kwargs):
    if len(kwargs) != 0:
        for key,item in sorted(kwargs.items()):
            print(f'{key}: {item}')


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 