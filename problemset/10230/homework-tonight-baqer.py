#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera

### https://quera.ir/problemset/10230/ ###

angles = input()

angles = angles.split(" ")
angles = angles[:3]

angles = [int(angle) for angle in angles]

sum_of_angles = sum(angles)

if 0 in angles or sum_of_angles != 180:
    message = "No"
else:
    message = "Yes"


print(message)
