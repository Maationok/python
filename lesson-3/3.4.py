print("Vvedite x")
x = float(input())
print("Vvedite y")
y = int(input())

print("x^y =", x ** y)


def stepen(x, y):
    stepen_x = 1
    for i in range(abs(y)):
        stepen_x *= x
    return 1 / stepen_x


if y < 0:
    print("x^y =", stepen(x, y))
else:
    print("y>=0")
