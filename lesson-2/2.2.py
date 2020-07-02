a = list(input())
print(a)
i = int(0)
while (i + 1) < len(a):
    s = a[i]
    a[i] = a[i + 1]
    a[i + 1] = s
    i += 2
print(a)
