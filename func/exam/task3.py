# Pretty print

# Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой. 

# Функция должна получать на вход один обязательный аргумент data – список, который следует вывести и два необязательных строковых односимвольных  аргумента side и delimiter и выводить содержимое списка в соответствии с примерами.

# В случае если отсутствует аргумент side, то полагаем side='-', а если отсутствует аргумент delimiter, то полагаем delimiter='|'.

# Примечание 1. Следующий программный код:

# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

# должен выводить:

#  ------------------------------ 
# | 1 | 2 | 10 | 23 | 123 | 3000 |
#  ------------------------------ 
#  ------------------------- 
# | abc | def | ghi | 12345 |
#  ------------------------- 
#  ***************** 
# | abc | def | ghi |
#  ***************** 
#  ----------------- 
# # abc # def # ghi #
#  ----------------- 
#  ***************** 
# # abc # def # ghi #
#  ***************** 

# Примечание 2. Вызывать функцию pretty_print() не нужно, требуется только реализовать.

# Примечание 3. Считайте, что side и delimiter состоят всегда из одного символа.

def pretty_print(data, side='-', delimiter='|'):
    borders = side * (sum([len(str(i)) for i in data])+2*len(data)+len(data)-1)
    s1 = list(map(str, data))
    m_delim = ' '+delimiter+' '
    print(' '+borders)
    print(f'{delimiter} {m_delim.join(s1)} {delimiter}')
    print(' '+borders)


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')




# соберу в один комментарий, что мне помогло из коментариев ниже

#     Тут | 1 | 2 | 10 | 23 | 123 | 3000 | 32 символа, а символов - 30 штук.
#     Тут | abc | def | ghi | 12345 | 27 символов, а символов - 25 штук.
#     Тут | abc | def | ghi | 19 символов, а символов * 17 штук.
#     f''.join(map(str, список)) так можно склеить список из чисел в строку, ф-строка там тоже не спроста
#     ну и главное пожалуй "Сначала в теле функции создайте переменную, в которой у вас будет лежать строка со значениями data, а уже потом распечатывайте все необходимые строки, с учетом длины строки из вашей переменной."

