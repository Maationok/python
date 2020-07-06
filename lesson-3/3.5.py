summa = 0
simvol = False
while simvol == False:
    print("Vvedite chisla, v - vihod")
    chisla = input("").split()
    for el in range(len(chisla)):
        if chisla[el] == 'v':
            simvol = True
            break
        summa += int(chisla[el])
    print("summa =", summa)
print("obshaya summa =", summa)
