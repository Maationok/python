class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        # methods

    def go(self):
        return self.name + " poehala"

    def stop(self):
        return self.name + " ostanovilas"

    def turn_right(self):
        return self.name + " povernula napravo"

    def turn_left(self):
        return self.name + " povernula nalevo"

    def show_speed(self):
        return "Tekushaya skorost " + self.name + " = " + str(self.speed)

    def police(self):
        if self.is_police:
            return self.name + " - policiya"
        else:
            return self.name + " - ne policiya"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "Tekushaya skorost " + self.name + " = " + str(self.speed) + " - skorost previshena!!! (>40)"
        else:
            return "Tekushaya skorost " + self.name + " = " + str(self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Tekushaya skorost " + self.name + " = " + str(self.speed) + " - skorost previshena!!! (>60)"
        else:
            return "Tekushaya skorost " + self.name + " = " + str(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


mashina1 = TownCar(50, "Siniy", "mashina1", False)
mashina2 = SportCar(300, "Krasniy", "mashina2", False)
mashina3 = WorkCar(150, "Zeleniy", "mashina3", False)
mashina4 = PoliceCar(40, "Beliy", "mashina4", True)

print(mashina1.go())
print(mashina2.turn_right())
print(mashina2.show_speed())
print(mashina3.show_speed())
print(mashina4.police())
print(mashina1.show_speed())
print(mashina2.turn_left())
print(mashina3.stop())
print(mashina4.show_speed())
print(mashina1.color)
