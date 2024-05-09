'''

CSV-файл

Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна содержать реализованную функцию read_csv.

Примечание 1. Вызывать функцию read_csv не нужно.

Примечание 2. Функция read_csv не должна принимать аргументов. 

Примечание 3. Подробнее прочитать про CSV-файлы можно тут.

Примечание 4. Считайте, что все ключи и значения по этим ключам в результирующем словаре имеют строковый тип (str).

Примечание 5. Указанный файл можно скачать по ссылке.

Примечание 6. Если бы файл data.csv содержал информацию

name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21

то вызов функции read_csv() вернул бы список:

[{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'}, {'name': 'John', 'address': '54 Love Ave', 'age': '21'}]


'''
def read_csv():
    lst=[]
    with open('files/data.csv',encoding='utf-8') as file:
        keys = file.readline().rstrip('\n').split(',')
        for i in file.readlines():
            a=i.rstrip('\n').split(',')
            lst+=[dict(zip(keys,a))]
    print(lst)
lst=[]

if __name__ == '__main__':
    read_csv()