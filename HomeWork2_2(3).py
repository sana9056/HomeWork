my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# решение для добавления 0
for i in range(len(my_list)):
    if my_list[i].isdigit():
        if int(my_list[i]) < 10:
            my_list[i] = '0' + my_list[i]
    else:
        new_list = list(my_list[i])
        for b in range(len(new_list)):
            if new_list[b].isdigit():
                if int(new_list[b]) < 10:
                    new_list.insert(b, '0')
                my_list[i] = "".join(new_list)
# костыльное решение для добавления ковычек, но в итоге выводит "как в задаче"
for i in range(len(my_list)):
    new_list = list(my_list[i])
    for c in range(len(new_list)):
        if new_list[c].isdigit():
            if int(new_list[c]) >= 0:
                new_list.insert(0, '"')
                new_list.insert(len(new_list), '"')
            my_list[i] = ''.join(new_list)
            break
print(*my_list, sep=' ')
