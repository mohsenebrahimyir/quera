#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/3539/ ###

def single_digit():
    number = input()
    number = int(number)

    while number > 9:
        number = str(number)
        digits = [int(digit) for digit in number]
        number = sum(digits)

    return number


if __name__ == '__main__':
    result = single_digit()
    print(result)
