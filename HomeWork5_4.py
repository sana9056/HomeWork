import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Использую comprehensions чтобы получить требуемый результат, оптимизировав по скорости
result = [src[i] for i in range(len(src)) if src[i - 1] < src[i]]
result.remove(300)  # костыль для нулевого объекта, который вставляется по ошибке.
print(type(result), sys.getsizeof(result))
print(result)
