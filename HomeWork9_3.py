class Worker:

    name = "Иван Иванович"
    surname = 'Иванов'
    position = 'Офисный клерк'
    __income = {"wage": 500,  "bonus": 100}
    wage = __income["wage"]
    bonus = __income["bonus"]


class Position(Worker):

    def get_full_name(self):
        print(f'Имя работника: {self.name} {self.surname} он занимает должность: {self.position}')

    def get_total_income(self):
        print(f'Работник: {self.name} получает доход: {self.wage + self.bonus}')


p = Position()
p.get_full_name()
p.get_total_income()
