#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera

### https://quera.ir/problemset/9774/ ###

number = input()

for digit in number:
    message = digit + ":"
    print(message, digit * int(digit))