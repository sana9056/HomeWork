class ComplexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.num_1 + other.num_1} + {self.num_2 + other.num_2} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.num_1 * other.num_1 - (self.num_2 * other.num_2)} + ' \
               f'{(self.num_2 * other.num_1) + (self.num_1 * other.num_2)} * i'

    def __str__(self):
        return f'z = {self.num_1} + {self.num_2} * i'


z_1 = ComplexNumber(7, 5)
z_2 = ComplexNumber(1, 8)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
