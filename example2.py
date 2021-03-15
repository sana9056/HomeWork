"""
Доп задача -> убрать [1,2,3] и заменить на элементы большого списка 1, 2, 3
в том же месте
Подсказка: index, insert, remove (опционально)
"""
test_list = ['Hello', 42.00000014, True, [1, 2, 3], 1, 2, 'Basil']
print(f'Первоначальный список: {test_list}')
b = test_list[3]
for i in range(len(b)):
    test_list.insert(i + 3, b[i])
test_list.remove(b)
print(f'Список изменённый: {test_list}')
