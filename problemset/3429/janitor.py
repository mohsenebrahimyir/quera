#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/3429/ ###


def samovar_temperature():
    temp = input()
    temp = int(temp)

    if temp > 100:
        message = "Steam"
    elif temp < 0:
        message = "Ice"
    else:
        message = "Water"

    return message

if __name__ == '__main__':
    result = samovar_temperature()
    print(result)
