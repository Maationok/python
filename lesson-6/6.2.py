class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rezultat(self):
        self.massa = 25
        self.tolshina = 5
        rezultat = self.length * self.width * self.massa * self.tolshina / 1000
        return rezultat


doroga = Road(5000, 20)
print(doroga.rezultat(), "tonn")
