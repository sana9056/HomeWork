from collections import OrderedDict

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = list(OrderedDict.fromkeys(src))
test_list = []
# Прежде чем найти класс Counter, я использовал данное решение "в лоб"
for i in range(len(src)):
    for j in src:
        if j in src:
            p = j
            src.remove(p)
            if p in src:
                while p in src:
                    src.remove(p)
                    test_list.append(p)
test_list = list(set(test_list))
for el in test_list:
    result.remove(el)
print(result)
