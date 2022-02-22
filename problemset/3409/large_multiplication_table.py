#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/3409/ ###


def multiple_table():
    n = input()
    n = int(n)

    cols = [i+1 for i in range(n)]
    table = []

    for i in cols:
        row = [str(i * col) for col in cols]
        table.append(" ".join(row))

    return "\n".join(table)


if __name__ == '__main__':
    result = multiple_table()
    print(result)
