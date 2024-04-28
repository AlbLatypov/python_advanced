# Условие https://stepik.org/lesson/356380/step/12?unit=340495

import random
n = int(input())
lst=[]
friend2=[]
for _ in range(n):
    lst += [i for i in input().strip().splitlines()]
for el in lst: #<---- el для каждого товарища
    any_not_me_ls=[i for i in lst if i != el] #<--- формируем список из оставшихся
    # выбираем случайного и добавляем его в список, тут нужно проверка что он в списке не состоит
    while True:
      tmp = any_not_me_ls[random.randrange(len(any_not_me_ls))]
      if tmp not in friend2:
        friend2.append(tmp)
        break
    print(f'{el} - {tmp}')
