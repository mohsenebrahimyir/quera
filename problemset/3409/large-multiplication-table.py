#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera

### https://quera.ir/problemset/3409/ ###

n = input()
n = int(n)

numbers_1_to_n = range(1, n+1)

for row in numbers_1_to_n:
    row_times_col = [str(row * col) for col in numbers_1_to_n]
    message = " ".join(row_times_col)
    print(message)
