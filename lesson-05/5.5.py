file = open('5.5.txt', 'w+')
chisla = input()
file.writelines(chisla)
chisla = chisla.split()
summa = 0
for i in range(len(chisla)):
    summa += int(chisla[i])
print(summa)
file.close()
