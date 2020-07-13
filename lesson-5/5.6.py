file = open('5.6.txt', 'r')
slovar = {}
for stroka in file:
    stroka = stroka.replace("—", "")
    stroka = stroka.replace("-", "")
    stroka = stroka.replace(":", "")
    predmeti = stroka.split()
    for el in range(len(predmeti) - 1):
        predmeti[el + 1] = predmeti[el + 1].replace("(", "")
        predmeti[el + 1] = predmeti[el + 1].replace(")", "")
        predmeti[el + 1] = predmeti[el + 1].replace("л", "")
        predmeti[el + 1] = predmeti[el + 1].replace("пр", "")
        predmeti[el + 1] = predmeti[el + 1].replace("л", "")
        predmeti[el + 1] = predmeti[el + 1].replace("а", "")
        predmeti[el + 1] = predmeti[el + 1].replace("б", "")
        predmeti[el + 1] = predmeti[el + 1].replace(".", "")
    # print(predmeti[0])
    chasi = 0
    for el in range(len(predmeti) - 1):
        # print(predmeti[el + 1])
        chasi += int(predmeti[el + 1])
    slovar[predmeti[0]] = chasi
print(slovar)
file.close()
