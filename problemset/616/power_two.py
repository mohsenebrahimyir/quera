#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/616/ ###

from math import ceil, log2

def power_2():
    n = input()
    n = int(n)

    log2_n = log2(n)
    ceil_log2_n = ceil(log2_n)

    return 2**ceil_log2_n

if __name__ == '__main__':
    result = power_2()
    print(result)