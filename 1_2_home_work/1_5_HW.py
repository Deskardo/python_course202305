# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

size = int(input('укажите желаемую длину массива: '))
j = 0

if size % 2 == 0:
    j = int(size/2)
else:
    j = int(size/2) + 1
    
arr = [random.randint(0, size) for i in range(size)]
arrComposition = [i for i in range(j)]
composition = 1
i = 0


print(arr)

while i < j:
    arrComposition[i] = int(arr[i]) * int(arr[-(i+1)])
    i += 1

print(arrComposition)
