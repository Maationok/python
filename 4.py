a = int(input())
b = 0
c = 0
while a > 0:
    b = a % 10
    a = a // 10
    if c < b:
        c=b
print(c)
