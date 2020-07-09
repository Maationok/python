def delenie(delimoe, delitel):
    if delitel != 0:
        return delimoe / delitel
    else:
        return "Delitel=0"


print("Vvedite delimoe")
delimoe = int(input())
print("Vvedite delitel")
delitel = int(input())
print(delenie(delimoe, delitel))
