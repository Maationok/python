import json

pribil = {}
sum_pribil = 0
k = 0
file = open('5.7.txt', 'r')
for stroka in file:
    nazvanie, forma, viruchka, izderzki = stroka.split()
    pribil[nazvanie] = int(viruchka) - int(izderzki)
    if pribil.setdefault(nazvanie) >= 0:
        sum_pribil += pribil.setdefault(nazvanie)
        k += 1
if k > 0:
    sred_pribil = sum_pribil / k
    print("Srednya pribil =", sred_pribil)
else:
    print("Sredney pribili net")
sred_pribil_dobavit = {'Srednya pribil': round(sred_pribil)}
# pribil.update(sred_pribil_dobavit)
spisok = [pribil, sred_pribil_dobavit]
print(spisok)
file2 = open('5.7.json', 'w')
json.dump(spisok, file2)
file.close()
file2.close()
