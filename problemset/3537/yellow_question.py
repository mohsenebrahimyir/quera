#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/3537/ ###


def says_wow():
    info_count = input()
    info_count = int(info_count)
    o = "o" * info_count
    message = "W" + o + "w!"

    return message


if __name__ == '__main__':
    result = says_wow()
    print(result)
