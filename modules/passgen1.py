from string import ascii_letters, digits,ascii_uppercase
import random
genstr = ascii_letters + digits
chars_to_remove = 'lIoO10'
table = str.maketrans('', '', chars_to_remove)
genstr = genstr.translate(table)
# LETTER = ''.join((set(ascii_letters) | set(digits)) - set('lI1oO0'))


def generate_password(length):
    # цифра верхний нижний
    passw = []
    while len(passw) < length or not any(i.isupper() for i in passw) or not any(i.islower() for i in passw) or not any(i.isdigit() for i in passw):
        passw = [genstr[random.randrange(len(genstr))] for _ in range(length)]
    return ''.join(passw)
    

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))
    return 
# n, m = int(input()), int(input()) # количество паролей, количество символов
generate_passwords(3,5)
