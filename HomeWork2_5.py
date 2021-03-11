count_of_sum = int(input('Введите желаемое количество цен:'))
my_list = []
for i in range(count_of_sum):
    my_list.append(float(input('Пожалуйста, введите сумму:')))
print(id(my_list))


def letter(in_list):
    for i in range(len(in_list)):
        ruble = int(in_list[i] // 1)
        penny = int((in_list[i] % 1) * 100)
        if penny < 10:
            penny = str('0' + str(penny))
        print(f'{ruble} руб {penny} коп,', end="")


# задание А
letter(my_list)
print()
# задание B
my_list.sort()
print(id(my_list))
# print(my_list)
letter(my_list)
print()
# задание C
rev_list = sorted(my_list, reverse=True)
letter(rev_list)
print()
# print(rev_list)
# задание D
max_list = rev_list[0:5]
letter(max_list)
print()
# print(max_list)
