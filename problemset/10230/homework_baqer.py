#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/10230/ ###


def can_make_triangle_with_angles():
    angles = input()
    angles = angles.split(" ")[:3]
    angles = [int(angle) for angle in angles]
    sum_of_angles = sum(angles)
    cannot_make = 0 in angles or sum_of_angles != 180
    message = "No" if cannot_make else "Yes"

    return message



if __name__ == '__main__':
    result = can_make_triangle_with_angles()
    print(result)
