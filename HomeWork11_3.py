class IntList:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                stop_word = input(f'Попробовать еще раз? Y/N ')

                if stop_word.lower() == 'y':
                    print(try_except.my_input())
                elif stop_word.lower() == 'n':
                    return f'Ок, выходим'
                else:
                    return f'Неверное значение, выкидываемся'


try_except = IntList()
print(try_except.my_input())
