# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

n = int(input())

arr = [randint(1, 5) for i in range(n)]
print(arr)

min = arr[0]
max = arr[0]

for i in range(n):          # находим максимум и минимум
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

for i in range(n):          # производим замену
    if arr[i] == max:
        arr[i] = min

print(arr)