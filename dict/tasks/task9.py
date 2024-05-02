'''
Дополните приведенный код так, 
чтобы в переменной result хранился словарь, в котором для каждого символа строки text будет подсчитано количество его вхождений.
'''
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for symbol in text:
    result[symbol] = result.get(symbol,0) + 1
print(result)

# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
#----------------------------------------------------------------------------------------------------
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

# result = {}
# for num in numbers:
#     if num not in result:
#         result[num] = 1
#     else:
#         result[num] += 1
