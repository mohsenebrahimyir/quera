#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera

### https://quera.ir/problemset/280/ ###

sides = []

while len(sides) < 3:
    side = input()
    side = int(side)
    sides.append(side)

sides.sort()

message = "YES" if sides[0]**2 + sides[1]**2 == sides[2]**2 else "NO"

print(message)