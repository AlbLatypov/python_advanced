ffile='data'

with open(ffile, encoding='utf-8') as f:
    temp = f.readlines()[-2:-1]
    print(temp[0].rstrip('\n'))


# [q:=open(input()), print(q.readlines()[-2]), q.close()]

# Этот код на Python выполняет следующие действия:

#     q:=open(input()) - открывает файл, имя которого вводится пользователем, и присваивает объект файла переменной q. Это использует оператор присваивания :=, который был введен в Python 3.8 и позволяет присваивать значение переменной в том же выражении.

#     print(q.readlines()[-2]) - читает все строки из открытого файла с помощью метода readlines(), который возвращает список строк. Затем выводится на печать предпоследняя строка из этого списка с помощью индекса -2.

#     q.close() - закрывает открытый файл с помощью метода close().

# Таким образом, этот код открывает файл, имя которого вводит пользователь, выводит на печать предпоследнюю строку этого файла и закрывает файл.

# Обратите внимание, что использование оператора присваивания := внутри выражения может затруднить чтение кода, поэтому его следует использовать с осторожностью и только в том случае, если это действительно улучшает читаемость кода.
