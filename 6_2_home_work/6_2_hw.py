# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

from random import randint

n = int(input('Введите длину списка: '))
a = [randint(-n, n+1) for i in range(n)]
max = int(input('Введите максимум: '))
min = int(input('Введите минимум: '))
print(a)
result = []


for i in range(len(a)):
    if min < a[i] < max:
        result.append(i)

print(result)