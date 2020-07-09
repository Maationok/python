from itertools import cycle

spisok = [1, 'a', 'b', 32, 43, 'c']
i = 0
for el in cycle(spisok):
    print(el)
    i += 1
    if i == 30:
        break
