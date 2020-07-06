print("Vvedite imya")
imya = input()
print("Vvedite familiu")
familiya = input()
print("Vvedite god rozdeniya")
god_rozdeniya = input()
print("Vvedite gorod prozivaniya")
gorod = input()
print("Vvedite email")
email = input()
print("Vvedite telefone")
telefon = input()


def polzovatel(imya, familiya, god_rozdeniya, gorod, email, telefon):
    return imya + ' ' + familiya + ' ' + god_rozdeniya + ' ' + gorod + ' ' + email + ' ' + telefon


print(polzovatel(imya, familiya, god_rozdeniya, gorod, email, telefon))
