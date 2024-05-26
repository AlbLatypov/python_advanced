z1 = 5 + 7j
z2 = 1j
z3 = -3 + 5J
z4 = 1.5 + 3.2j

print(z1, z2, z3, z4, sep='\n')
print(type(z1))

numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]

a = max(numbers, key = complex())

print(complex(a))
