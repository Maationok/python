from itertools import count

print("Vvedite ukazannoe chislo")
chislo = int(input())
for el in count(chislo):
    print(el)
    if el == chislo + 30:
        break
