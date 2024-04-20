import sys

# Проверка на наличие аргумента командной строки
if len(sys.argv) < 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

# Получение пути к файлу из аргумента командной строки
file_path = sys.argv[1]

# Открыть файл для чтения
counter=0
summ=0
try:
    with open(file_path, 'r') as file:
        for i in file.readlines():
            lst=i.rstrip('\n').split()
            summ+=float(lst[0])
            counter+=1
    print(f'{summ/counter:.2f}')
    # print(counter)      
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
