#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/10162/ ###


def bala_or_payin_barare():
    k = input()
    k = int(k)

    message = "Bala" if k % 2 == 0 else "Payin"
    message += " Barare"

    return message



if __name__ == '__main__':
    result = bala_or_payin_barare()
    print(result)