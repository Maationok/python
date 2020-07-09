from functools import reduce


def ymnozenie(el, el_2):
    return el * el_2


print([el for el in range(99, 1001) if el % 2 == 0])
print(reduce(ymnozenie, [el for el in range(99, 1001) if el % 2 == 0]))
