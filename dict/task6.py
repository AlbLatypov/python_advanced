'''
Код Морзе

Код Морзе для представления цифр и букв использует тире и точки.

Напишите программу для кодирования текстового сообщения в соответствии с кодом Морзе.
Символ 	Код 	Символ 	Код 	Символ 	Код 	Символ 	Код
A 	.- 	J 	.--- 	S 	... 	1 	.----
B 	-... 	K 	-.- 	T 	- 	2 	..---
C 	-.-. 	L 	.-.. 	U 	..- 	3 	...--
D 	-.. 	M 	-- 	V 	...- 	4 	....-
E 	. 	N 	-. 	W 	.-- 	5 	.....
F 	..-. 	O 	--- 	X 	-..- 	6 	-....
G 	--. 	P 	.--. 	Y 	-.-- 	7 	--...
H 	.... 	Q 	--.- 	Z 	--.. 	8 	---..
I 	.. 	R 	.-. 	0 	----- 	9 	----.

Формат входных данных
На вход программе подается одна строка – текстовое сообщение.

Формат выходных данных
Программа должна вывести закодированное с помощью кода Морзе сообщение, оставляя пробел между каждым закодированным символом (последовательностью тире и точек).

Примечание 1. Ваша программа должна игнорировать любые символы, не перечисленные в таблице.

Примечание 2. Код Морзе был разработан в XIX веке и все еще используется, спустя более 160160 лет после создания.
'''

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', 
         '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', 
         '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', 
         '....-', '.....', '-....', '--...', '---..', '----.']

m_input=input().upper().strip(' !?+-,.')
m_dict = dict(zip(letters, morse))
for i in m_input:
    for key,value in m_dict.items():
        if i==key:
            print(value, end=' ')

result = {}
for i in range(1,16):
    result.update({i:i**i})

print(result)
