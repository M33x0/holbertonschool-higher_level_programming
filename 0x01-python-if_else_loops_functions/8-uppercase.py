#!/usr/bin/python3
def uppercase(str):
    for c in str:
        f = 0
        if ord(c) >= 97 and ord(c) <= 122:
            f = 32
        print('{:c}'.format(ord(c) - f), end="")
    print()
