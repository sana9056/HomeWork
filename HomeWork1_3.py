declination_list = ["процент", "процента", "процентов"]
my_number = int(input('Пожалуйста введите число от 1 до 20:'))
if my_number == 1:
    print(f'Вы получили {my_number} {declination_list[0]} .')
elif my_number <= 4:
    print(f'Вы получили {my_number} {declination_list[1]} .')
else:
    print(f'Вы получили {my_number} {declination_list[2]} .')
print(f'Все используемые склонения {declination_list} .')
