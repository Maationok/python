class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Zapusk otrisovki."


class Pen(Stationary):
    def draw(self):
        return "Zapusk otrisovki ruchkoy."


class Pencil(Stationary):
    def draw(self):
        return "Zapusk otrisovki karandashom."


class Handle(Stationary):
    def draw(self):
        return "Zapusk otrisovki markerom."


ruchka = Pen("ruchka")
karandash = Pencil("karandash")
marker = Handle("marker")
mel = Stationary("mel")
print(ruchka.draw())
print(karandash.draw())
print(marker.draw())
print(mel.draw())
