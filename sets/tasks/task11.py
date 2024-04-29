'''
Используя генератор множеств, дополните приведенный код так, чтобы получить множество, содержащее уникальные слова (в нижнем регистре) строки sentence. 
Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.

Примечание. Учтите, что знаки пунктуации не относятся к словам.
'''

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, 
nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), 
the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or 
suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''



# Можно использовать words = [word.lower().strip('.,;:-?!') for word in input().split()]
# или так
# import re
# str1=input().lower()
# str1 = re.sub(r'[.,!?:;-]', '', str1)
# m_set = set(str1.split(' '))
# print(len(m_set))
#----------------------------------------------------------------------------------


# Решение: все решения ниже имеют право быть!
# m_list = set([words.lower().strip('().,;:-?!') for words in sentence.split()])
# m_list = {words.lower().strip('().,;:-?!') for words in sentence.split()}
# m_list = {words.strip('().,;:-?!') for words in sentence.lower().split()}
# print(*sorted(m_list))

# вывести 4 первых буквы каждого слова
w_length=4
m_list = {words.strip('().,;:-?!') for words in sentence.lower().split() if len(words.strip('().,;:-?!')) < w_length}
print(len(m_list))
print(*sorted(m_list))
