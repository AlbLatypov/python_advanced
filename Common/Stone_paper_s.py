Tim=input()
Rus=input()

#Камень закрывает бумагу, ножницы режут бумагу, ножницы тупятся об камень

dct={('бумага', 'камень'):'бумага',
     ('бумага', 'ножницы'):'ножницы',
     ('камень', 'ножницы'):'камень',
     }
get_result={Tim:'Тимур',Rus:'Руслан'}
# a=dct.get({Tim,Rus},'ничья')
result=get_result.get(dct.get(tuple(sorted((Tim,Rus))),'ничья'),'ничья')

print(result)
