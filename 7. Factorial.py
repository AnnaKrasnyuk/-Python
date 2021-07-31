from itertools import count
from functools import reduce


def fact(n):
    res = 1
    for i in count(1):
        if i <= n:
            res *= i
            yield res
        else:
            break


n = int(input("Факториал какого числа искать? "))
for el in fact(n):
    print(el)
