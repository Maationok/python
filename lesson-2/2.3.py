n = int(input())
a = ['zima', 'vesna', 'leto', 'osen']
b = {1: 'zima', 2: 'vesna', 3: 'leto', 4: 'osen'}
if n == 1 or n == 2 or n == 12:
    print(a[0])
    print(b.get(1))
if n == 3 or n == 4 or n == 5:
    print(a[1])
    print(b.get(2))
if n == 6 or n == 7 or n == 8:
    print(a[2])
    print(b.get(3))
if n == 9 or n == 10 or n == 11:
    print(a[3])
    print(b.get(4))
if n < 1 or n > 12:
    print("Net takogo mesyasa")
