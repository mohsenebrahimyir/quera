#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/87176/ ###

def game(number):
    numbers = [int(i) for i in str(number)]
    tafazol = numbers[1] - numbers[0]
    return abs(tafazol)


if __name__ == '__main__':
    result = game(17)
    print(result)