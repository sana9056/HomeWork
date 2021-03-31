from collections import Counter
# тк я нашел отличный модуль и класс я решил использовать их для "оптимицазии" выполнения задачи
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
cnt = Counter(src)
res = [el for el in src if cnt[el] == 1]
print(res)
