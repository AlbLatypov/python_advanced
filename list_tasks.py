# Разбиение на чанки 🌶️
#
# На вход программе подаются две строки: на одной – символы, на другой – число nn. Из первой строки формируется список.
#
# Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает
# список из чанков (кусков) указанной длины.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела и число nn на отдельной
# строке.
#
# Формат выходных данных
# Программа должна вывести указанный вложенный список.


def chunkss(base_list: list, result_list: list, n_chunks: int):
    if len(base_list) == 0:
        return
    else:
        if len(base_list) > n_chunks:
            result_list += [[base_list.pop(0) for _ in range(n_chunks)]]
        else:
            result_list += [[base_list.pop(0) for _ in range(len(base_list))]]
        # print(base_list)
        chunkss(base_list, result_list, n_chunks)
        return result_list


a = input().split()
b = int(input())
print(chunkss(a, [], b))
