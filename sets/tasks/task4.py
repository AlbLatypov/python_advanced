'''
На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке. 

Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.

Формат входных данных
На вход программе подаются натуральное число n≥1n≥1, а затем nn различных натуральных чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести цифры в соответствии с условием задачи. Если общих цифр нет, то ничего выводить не нужно.
'''
amount_numbers = int(input())
m_list = [set(input()) for _ in range(amount_numbers)]
for i in range(1,len(m_list)):
    m_list[0] &= m_list[i]
print(*sorted(map(int, m_list[0])))
#это должны быть пересечения &=

# # код преподавателя
# n = int(input())

# # инициализируем результирующее множество как множество цифр первой строки
# s = set(input())
# for _ in range(n - 1):
#     cur_s = set(input())
#     s &= cur_s
# print(*sorted(s))
