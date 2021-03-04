my_list = []
for i in range(1, 1000, 2):
    my_list.append(i ** 3)
sum_counter = 0
sum_of_number = 0
print("Список, состоящий из кубов нечётных чисел от 0 до 1000:")
print(my_list)
#Выполнение условия А второй задачи
for i in range(0, len(my_list), 1):
    count = my_list[i]
    while my_list[i] > 0:
        sum_of_number += my_list[i] % 10
        my_list[i] = my_list[i] // 10
    if sum_of_number % 7 == 0:
        sum_counter += count
    my_list[i] = count + 17 #Выполнение условия С второй задачи
    sum_of_number = 0
print("Число, которое получается в сумме чисел, сумма цифр которых делится нацело на 7 равна:")
print(sum_counter)
# my_list.clear()
# for i in range(1, 1000, 2):
#     my_list.append((i ** 3) + 17)
print("Если к первоначальному виду списка чисел прибавить 17, выйдет следующий список чисел:")
print(my_list)
#Выполнение условия B второй задачи
for i in range(0, len(my_list), 1):
    count = my_list[i]
    while my_list[i] > 0:
        sum_of_number += my_list[i] % 10
        my_list[i] = my_list[i] // 10
    if sum_of_number % 7 == 0:
        sum_counter += count
print("Число, которое получается в сумме чисел, сумма цифр которых делится нацело на 7 равна:")
print(sum_counter)

