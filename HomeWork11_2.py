class DevOnNull:

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def whack_on_null(num_1, num_2):
        try:
            return num_1 / num_2
        except:
            return f'Деление на 0 недопустимо'


print(DevOnNull.whack_on_null(10, 0))
print(DevOnNull.whack_on_null(10, 1))
