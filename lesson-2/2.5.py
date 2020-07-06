a = [7, 5, 5, 3, 3, 2, 1]
print(a)
print("Vvedite novii element reitinga")
b = int(input())
for el in range(len(a)):
    if a[el] == b:
        a.insert(el + 1, b)
        break
    if a[0] < b:
        a.insert(0, b)
        break
    if a[-1] > b:
        a.append(b)
        break
    if a[el] > b and a[el + 1] < b:
        a.insert(el + 1, b)
        break
print(a)
