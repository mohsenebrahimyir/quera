#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/589/ ###

def factorial():
    n = input()
    n = int(n)

    fact = 1
    for i in range(n):
        fact *= n - i

    return fact


if __name__ == '__main__':
    result = factorial()
    print(result)
