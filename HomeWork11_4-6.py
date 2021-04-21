from abc import ABC, abstractmethod


class Stock:
    def __init__(self, stc_name):
        self.stock_dir = []
        self.stc_name = stc_name

    # Задание 5 добавние товара на склад
    def add_equip(self, obj):
        try:
            unique = {'Модель устройства': obj.name, 'Цена за ед': obj.price, 'Количество': obj.quantity}
            self.stock_dir.append(unique)
        except:
            return f'Ошибка ввода данных'

    def __str__(self):
        print(f'\n      Весь склад {self.stc_name}:')
        for i in range(len(self.stock_dir)):
            print(f'{self.stock_dir[i]}')
        return f'     Конец списка склада.'

    # Задание 5 перемешение товара со склада на фирму (другой склад)
    def take_equip_to(self, name, other):
        for i in range(len(self.stock_dir)):
            equip = self.stock_dir[i]
            if name == equip['Модель устройства']:
                other.stock_dir.append(equip)
                return self.stock_dir.remove(equip)

    def __getitem__(self, item):
        return item


class OfficeEquipment(ABC):

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        # Задание 6 Валидация кол-ва товара
        if not isinstance(self.quantity, int):
            raise ValueError("Значение не является целым числом")

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


class Printer(OfficeEquipment):
    type = 'Принтер'


class Scanner(OfficeEquipment):
    type = 'Сканнер'


class Copier(OfficeEquipment):
    type = 'Ксерокс'


# Объявление новых вещей
printer_1 = Printer("Принтер Canon", 125, 12)
scanner_1 = Scanner("Сканер Canon", 100, 5)
copier_1 = Copier("Ксерокс Canon", 75, 3)
# Показываем один из предметов
print(printer_1)
# Объявляем Склад Склад
stock_1 = Stock('Склад')
# Добавляем в Склад вещи
Stock.add_equip(stock_1, printer_1)
Stock.add_equip(stock_1, scanner_1)
Stock.add_equip(stock_1, copier_1)
print(stock_1)
# Объявляем ещё один склад Офис
stock_2 = Stock("Офис")
# Перемещаем со Склада в Офис принтеры
stock_1.take_equip_to("Принтер Canon", stock_2)
# Показываем результат
print(stock_1)
print(stock_2)
