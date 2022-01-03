# !/user/bin/python
# Github: https://github.com/mohsenebrahimyir/quera

### Quera: https://quera.ir/problemset/2885/ ###

line_count = input()
line_count = int(line_count)

line_count_minus_1 = line_count - 1

hi_says = "man khoshghlab hastam"

message = hi_says + ("\n" + hi_says) * line_count_minus_1

print(message)
