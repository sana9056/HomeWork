class Cell:
    def __init__(self, cell_value):
        self.cell_value = cell_value

    def __add__(self, other):
        sum_value = self.cell_value + other.cell_value
        return sum_value

    def __sub__(self, other):
        sub_value = self.cell_value - other.cell_value
        if sub_value > 0:
            return sub_value
        else:
            return f'Значение ниже нуля, выполнить невозможно'

    def __mul__(self, other):
        mul_value = self.cell_value * other.cell_value
        return mul_value

    def __floordiv__(self, other):
        floor_value = self.cell_value // other.cell_value
        return floor_value

    def __truediv__(self, other):
        truediv_value = self.cell_value / other.cell_value
        return truediv_value

    def __str__(self):
        return self.cell_value

    def make_order(self, row):
        calc_cell_value = self.cell_value
        str_value = ''
        while calc_cell_value != 0:
            if calc_cell_value > row:
                str_value = str_value + '*' * row + '\n'
                calc_cell_value = calc_cell_value - row
            else:
                str_value = str_value + ('*' * calc_cell_value) + '\n'
                calc_cell_value = 0
        return str_value


cell_1 = Cell(10)
cell_2 = Cell(5)
cell_3 = Cell(15)
cell_4 = cell_1 + cell_2
# Тестирование работы методов:
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 - cell_3)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1 // cell_2)
print(cell_4)
print('\n')
print(f'Организация ячеек по рядам:\n{cell_1.make_order(4)}')
