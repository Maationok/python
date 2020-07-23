from random import randint


def generator_randomnih_chisel(dlina):
    spisok_chisel = []
    while len(spisok_chisel) < dlina:
        novoe_chislo = randint(1, 90)
        if novoe_chislo not in spisok_chisel:
            spisok_chisel.append(novoe_chislo)
    return spisok_chisel


class Kartochka:
    def __init__(self):
        kartochka_chisla = generator_randomnih_chisel(15)

        self.kartochka_postroenie = []
        for i in range(0, 3):
            stroka = sorted(kartochka_chisla[5 * i: 5 * (i + 1)])
            for j in range(0, 4):
                index = randint(0, len(stroka))
                stroka.insert(index, 0)
            self.kartochka_postroenie += stroka

    def __str__(self):
        kartochka_vivod = "--------------------------\n"
        for index, num in enumerate(self.kartochka_postroenie):
            if num == 0:
                kartochka_vivod += "  "
            elif num == -1:
                kartochka_vivod += " -"
            elif num < 10:
                kartochka_vivod += " " + str(num)
            else:
                kartochka_vivod += str(num)

            if (index + 1) % 9 == 0:
                kartochka_vivod += "\n"
            else:
                kartochka_vivod += " "

        return kartochka_vivod + "--------------------------"

    def __contains__(self, item):
        return item in self.kartochka_postroenie

    def zacherknut(self, num):
        for index, item in enumerate(self.kartochka_postroenie):
            if item == num:
                self.kartochka_postroenie[index] = -1
                return

    def zakrit(self) -> bool:
        return set(self.kartochka_postroenie) == {0, -1}


class Igra:
    bochenki = []

    def __init__(self):
        self.kartochka_igroka = Kartochka()
        self.katrochka_computera = Kartochka()
        self.bochenki = generator_randomnih_chisel(90)

    def danniy_hod(self) -> int:
        bochenok = self.bochenki.pop()
        print("Новый бочонок: " + str(bochenok) + " (осталось " + str(len(self.bochenki)) + ")")
        print("----- Ваша карточка ------\n" + str(self.kartochka_igroka))
        print("-- Карточка компьютера ---\n" + str(self.katrochka_computera))
        print("Зачеркнуть цифру? (y/n)")
        otvet_igroka = input().lower().strip()
        if otvet_igroka == "y" and not bochenok in self.kartochka_igroka or \
                otvet_igroka != "y" and bochenok in self.kartochka_igroka:
            return 2

        if bochenok in self.kartochka_igroka:
            self.kartochka_igroka.zacherknut(bochenok)
            if self.kartochka_igroka.zakrit():
                return 1
        if bochenok in self.katrochka_computera:
            self.katrochka_computera.zacherknut(bochenok)
            if self.katrochka_computera.zakrit():
                return 2

        return 0


igra = Igra()
while True:
    rezultat = igra.danniy_hod()
    if rezultat == 1:
        print("Вы выиграли!!!")
        break
    elif rezultat == 2:
        print("Компьютер выиграл!")
        break
