#!/usr/bin/python3
#Использование ls -la | ./scr2.py

import sys

for line in sys.stdin:
    # print(f'   {line.rstrip()}')
    if "Apr" in line.split():
        print(line)
    # print(f'{line.startswith("d")}')


