print("Vvedite virabotku v chasah")
virabotka = int(input())
print("Vvedite stavku v chas")
stavka = int(input())
print("Vvedite premiu")
premiya = int(input())


def zarplata(virabotka, stavka, premiya):
    return virabotka * stavka + premiya


print("Zarplata = ", zarplata(virabotka, stavka, premiya))
