# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A[i]
# Последняя строка содержит число X

from random import randint

n = int(input('Введите длину масива: '))
a = [randint(1, n) for i in range(n)]
print(a)
x = int(input('Введите число x для поиска: '))
count = 0

for i in range(n):
    if a[i] == x:
        count +=1
        
print(f'число {x} встречается {count} раз(а)')