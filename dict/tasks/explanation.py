
dct = {} 
for o in range(int(input())):
    a,b,c = input().split()
    store_or_create = dct.setdefault(a,{})
    store_or_create[b] = store_or_create.get(b,0) + int(c)
    # store_or_create[b] = store_or_create.get(b,int(c))
print(dct)
# for key, val in sorted(buyers.items()):
#     print(f'{key}:', *[f'{item} {quantity}' for item, quantity in sorted(val.items())], sep='\n')


# get(key[, default])

#     Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.

# setdefault(key[, default])

#     If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.


#     buyer, item, quantity = input().split()
#     # 1. в основной словарь вносим ключ buyer, если в нем ничего не хранится - возвращаем значение, если нет - пустой словарь
#     # 2. По сути это формирование словаря с новым ключом и возвращение из имеющегося словаря значения ранее, если есть
#     #
#     b_data = buyers.setdefault(buyer, {}) # <----- каждую итерацию в b_data значение ключа покупатель
#     print(f'------------------Итерация {o}-----------------')
#     print(f'Покупатель: {buyer}, b_data: тип {type(b_data)}. Значение - {item} {quantity}')
#     print(f'buyers до: тип {type(buyers)}. Значение - {buyers}')
#     b_data[item] = b_data.get(item, 0) + int(quantity)
#     print(f'buyers после: тип {type(buyers)}. Значение - {buyers}')
# print(buyers)
