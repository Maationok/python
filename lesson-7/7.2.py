class Odezda:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def tkan_palto(self):
        return "Tkani na palto = " + str(self.V / 6.5 + 0.5)

    def tkan_kostum(self):
        return "Tkani na kostum = " + str(self.H * 2 + 0.3)

    @property
    def tkan_vsego(self):
        return "Obshaya ploshad tkani = " + str((self.V / 6.5 + 0.5) + (self.H * 2 + 0.3))


class Palto(Odezda):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.tkan_na_palto = self.V / 6.5 + 0.5

    def __str__(self):
        return "Ploshad na palto = " + str(self.tkan_na_palto)


class Kostum(Odezda):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.tkan_na_kostum = self.H * 2 + 0.3

    def __str__(self):
        return "Ploshad na kostum = " + str(self.tkan_na_kostum)


palto = Palto(1, 0)
kostum = Kostum(0, 2)
odezda = Odezda(1, 2)
print(palto)
print(kostum)
print(palto.tkan_palto())
print(kostum.tkan_kostum())
print(odezda.tkan_vsego)
