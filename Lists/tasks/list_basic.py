# Список - это упорядоченный набор элементов, каждый из которых имеет свой номер (индекс). 
# Упорядоченный список - это коллекция, которая позволяет хранить элементы в определенном порядке.
# Список - это динамический массив, который может хранить элементы любого типа.
#списки в Python представляют собой массив ссылок. 
# каждый элемент такого массива хранит не сами данные, а ссылку на их расположение в памяти компьютера!
#каждый элемент имеет 4 секции: свой адрес в памяти, данные, адрес следующего элемента и адрес предыдущего элемента.шв

#срезы
#a=[1,4,7,9,12,32]
#a[2:5:2]  -->   [7, 12], где 2 - начало индекса среза, 5 - окончание индекса среза (не вкл), шаг среза

# enumerate() для получения как индекса, так и значений напрямую.
a=[10, 20, 30]
for i,v in enumerate(a):
    print(i,v)

#map+lambda
a = [10,20,30]
print(list(map(lambda x: x**2,a)))



