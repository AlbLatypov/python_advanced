# В Python словари (dictionaries) являются неупорядоченными коллекциями, 
# в которых данные хранятся в виде пар "ключ-значение". Ключи в словаре используются для доступа к соответствующим значениям. 
# Ниже приведены типы данных, которые могут использоваться в качестве ключей словаря в Python:

#     Непеременные типы данных (immutable types):
#         Числа (int, float, complex)
#         Строки (str)
#         Булевы значения (bool)
#         NoneType
#         Фrozenset
#         Tuple (неизменяемый тип списка)

#     Пользовательские классы, реализующие метод hash() и метод eq() (для сравнения ключей).

# Обратите внимание, что вы не можете использовать изменяемые типы данных (например, списки или словари) 
# в качестве ключей словаря, так как их значение может измениться, что нарушит принцип неизменности ключей в словаре.



#интересный способ отражение в словаре условий. В качестве ключа bool

def well(x):
    g=int(0)
    for s in x:
        if s=="good":g+=1
        if g>2:break
    return {g==0:"Fail!",g>0 and g<3:"Publish!",g>2:"I smell a series!"}[True]
