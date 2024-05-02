buyers = {}
for _ in range(int(input())):
    buyer, item, quantity = input().split()
    b_data = buyers.setdefault(buyer, {})
    b_data[item] = b_data.get(item, 0) + int(quantity)

for key, val in sorted(buyers.items()):
    print(f'{key}:', *[f'{item} {quantity}' for item, quantity in sorted(val.items())], sep='\n')
