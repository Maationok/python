print("Vvedite viruchku")
a = int(input())
print("Vvedite izdershki")
b = int(input())
if a > b:
    print("Pribil'")
    print("Rentabelnost'=",(a-b)/a)
    print("Vvedite kolichestvo sotrudnikov")
    n=int(input())
    print("Pribil'/Sotrudniki=",(a-b)/n)
else:
    print("Ubitok")
