#!/usr/bin/python3
# Github: https://github.com/mohsenebrahimyir/quera
### https://quera.ir/problemset/83360/ ###

def match_search():
    kwrd = input()
    srch = input()
    result = 1 if kwrd in srch else 0
    return result


if __name__ == '__main__':
    result = match_search()
    print(result)