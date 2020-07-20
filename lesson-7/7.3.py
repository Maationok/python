class Kletka:
    def __init__(self, kolichestvo):
        self.kolichestvo = int(kolichestvo)

    def __str__(self):
        return "kolichestvo yacheek: " + str(self.kolichestvo * "*")

    def __add__(self, other):
        return Kletka(self.kolichestvo + other.kolichestvo)

    def __sub__(self, other):
        if (self.kolichestvo - other.kolichestvo) > 0:
            return Kletka(self.kolichestvo - other.kolichestvo)
        else:
            return "Vichitanie nevozmozno! Raznost <0"

    def __mul__(self, other):
        return Kletka(int(self.kolichestvo * other.kolichestvo))

    def __truediv__(self, other):
        return Kletka(round(self.kolichestvo // other.kolichestvo))

    def make_order(self, v_ryadu):
        ryad = ''
        for i in range(int(self.kolichestvo / v_ryadu)):
            ryad += str("*" * v_ryadu) + "\\n"
        ryad += str("*" * (self.kolichestvo % v_ryadu))
        return ryad


kletka1 = Kletka(7)
kletka2 = Kletka(4)
print("kletka1:", kletka1)
print("kletka2:", kletka2)
print("kletka1+kletka2:", kletka1 + kletka2)
print("kletka1-kletka2:", kletka1 - kletka2)
print("kletka2-kletka1:", kletka2 - kletka1)
print("kletka1*kletka2:", kletka2 * kletka1)
print("kletka1/kletka2:", kletka1 / kletka2)
print("kletka1:", kletka1.make_order(3))
print("kletka2:", kletka2.make_order(2))
