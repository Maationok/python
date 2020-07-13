file = open('5.3.txt', 'r')
stroki = file.readlines()
summa = 0
for i in range(len(stroki)):
    stroka = stroki[i].split()
    if int(stroka[1]) < 20000:
        print(stroka[0])
    summa += int(stroka[1])
print("Sredniy dohod =", summa / len(stroki))
file.close()
