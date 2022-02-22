#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/280/ ###

def pythagorean():
    sides = []
    while len(sides) < 3:
        side = input()
        side = int(side)
        sides.append(side)

    sides.sort()
    is_right_triangle = sides[0]**2 + sides[1]**2 == sides[2]**2
    message = "YES" if is_right_triangle else "NO"

    return message


if __name__ == '__main__':
    result = pythagorean()
    print(result)