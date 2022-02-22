#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/102248/ ###

def compare(string1, string2):
    string1 = list(string1)
    string2 = list(string2)

    while True:
        if string1[0] < string2[0]:
            string1.pop(0)
        elif string1[0] > string2[0]:
            string2.pop(0)
        else:
            string1.pop(0)
            string2.pop(0)

        if len(string1) == 0 and len(string2) != 0:
            message = "".join(string2)
            break
        elif len(string1) != 0 and len(string2) == 0:
            message = "".join(string1)
            break
        elif len(string1) == 0 and len(string2) == 0:
            message = "Both strings are empty!"
            break
        else:
            string1 = list(reversed(string1))
            string2 = list(reversed(string2))

    return message


if __name__ == '__main__':
    result = compare('ali', 'salib')
    print(result)
