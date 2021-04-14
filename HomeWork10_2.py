from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, type_cloth):
        self.name = name
        self.type_cloth = type_cloth

    @abstractmethod
    def calc_fabrics(self, value):
        pass


class Coat(Clothes):
    def calc_fabrics(self, value):
        sum_value = 0
        if self.type_cloth == 'Пальто':
            sum_value = ((value/6.5) + 0.5)
            sum_value = round(sum_value, 2)
        else:
            print('Вы пытаетесь расчитать объем расхода ткани для Костюма')
        return sum_value


class Suit(Clothes):
    def calc_fabrics(self, value):
        sum_value = 0
        if self.type_cloth == 'Костюм':
            sum_value = ((2 * value) + 0.5)
        else:
            print('Вы пытаетесь расчитать объем расхода ткани для Пальто')
        return sum_value


clot_1 = Suit('Маржильер', 'Костюм')
calc_1 = clot_1.calc_fabrics(1.8)
clot_2 = Coat('Шевьер', 'Пальто')
calc_2 = clot_2.calc_fabrics(54)
calc_3 = calc_1 + calc_2
print(f'Расход ткани для {clot_1.type_cloth} {clot_1.name}: {calc_1}')
print(f'Расход ткани для {clot_2.type_cloth} {clot_2.name}: {calc_2}')
print(f'Расход ткани Общий: {calc_3}')
