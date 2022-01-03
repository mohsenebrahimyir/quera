#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera

### https://quera.ir/problemset/3429/ ###

temperature = input()
temperature = int(temperature)

if temperature > 100:
    message = "Steam"
elif temperature < 0:
    message = "Ice"
else:
    message = "Water"

print(message)
