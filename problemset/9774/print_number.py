#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/9774/ ###


def print_num():
    num = input()
    num = str(num)
    message = []
    for d in num:
        row = f"{d}:" if d == "0" else f"{d}: " + d * int(d)
        message.append(row)

    message = "\n".join(message)
    return message


if __name__ == '__main__':
    result = print_num()
    print(result)
