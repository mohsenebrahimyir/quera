#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/129728/ ###

print(' '.join(sorted([(i if (ord(i) - 97) % 2 == 0 else i.upper()) for i in input()], reverse=True)))
