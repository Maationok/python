a = input()
b = []
n = 1
for el in range(a.count(' ') + 1):
    b = a.split()
    if len(str(b)) <= 10:
        print(f" {n} {a[el]}")
        n += 1
    else:
        print(f" {n} {b[el][0:10]}")
        n += 1
