from itertools import count
from math import factorial

print("Vvedite chislo n")
n = int(input())


def fact(i):
    for i in count(1):
        yield factorial(i)


for el in fact(n):
    if n > 0:
        print(el)
        n -= 1
    else:
        break
