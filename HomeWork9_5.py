class Stationery:
    title = 'Пишущий инструмент'

    def draw(self):
        print(f'Начата отрисовка с помощью {self.title}.')


class Pen(Stationery):
    title = 'Ручка'

    def draw(self):
        print(f'Начата отрисовка с помощью {self.title}, линия прямая и аккуратная.')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print(f'Начата отрисовка с помощью {self.title}, линия тонкая и её можно стереть.')


class Handle(Stationery):
    title = 'Супер Ручка'

    def draw(self):
        print(f'Начата отрисовка с помощью {self.title}, на самом деле это тоже ручка, но прикольнее.')


t = Stationery()
p = Pen()
pp = Pencil()
h = Handle()

t.draw()
p.draw()
pp.draw()
h.draw()
