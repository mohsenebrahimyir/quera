#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/129726/ ###

def is_even(i):
    return True if i % 2 == 0 else False


def separator(ls):
    odd, even = [], []

    for i in ls:
        if is_even(i):
            even.append(i)
        else:
            odd.append(i)

    return (even, odd)


if __name__ == '__main__':
    separator()
