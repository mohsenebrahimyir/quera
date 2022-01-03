#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera

### https://quera.ir/problemset/589/ ###

n = input()
n = int(n)

factorial = 1

for i in range(n):
    factorial *= n - i


print(factorial)
