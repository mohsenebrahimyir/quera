#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### Quera: https://quera.ir/problemset/2885/ ###


def man_khoshghlab_hastam():
    line_count = input()
    line_count = int(line_count)
    line_count_minus_1 = line_count - 1
    says = "man khoshghlab hastam"
    message = says + ("\n" + says) * line_count_minus_1

    return message


if __name__ == '__main__':
    result = man_khoshghlab_hastam()
    print(result)
