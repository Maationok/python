class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income.get('wage') + self.income.get('bonus')


dannie = Position('Ivan', 'Ivanov', 'Director', 80000, 20000)
print(dannie.get_full_name())
print(dannie.get_total_income())
print(dannie.position)
# print(dannie.income)
