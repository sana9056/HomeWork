class Date:

    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def date_to_int(cls, obj):
        obj = obj.str_date.split('-')
        return int(obj[0]), int(obj[1]), int(obj[2])

    @staticmethod
    def valid_date(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Верная дата'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Date.date_to_int(self.str_date)}'


date_1 = Date('12-03-1996')
print(Date.date_to_int(date_1))
print(Date.valid_date(12, 3, 1996))
print(Date.valid_date(12, 15, 1996))
print(Date.valid_date(15, 3, 2025))
print(Date.valid_date(72, 3, 1996))
