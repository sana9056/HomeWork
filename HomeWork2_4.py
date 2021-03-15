my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(my_list)):
    count_1 = i
    count_2 = i + 1
    new_list = my_list[count_1:count_2]
    new_list = new_list[0]
    # print(new_list)
    name_list = new_list.split()
    # print(name_list)
    name = name_list[-1].capitalize()
    print(f'Приветствую, {name}.')






