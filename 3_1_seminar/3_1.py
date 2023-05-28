# Дан список чисел. Определите, сколько в нем встречается различных чисел.

from random import randint

n = 5
arr1 = [randint(1, 5) for i in range(n)]
arr2 = []
print(arr1)

for i in range(n):
    if arr1[i] not in arr2:
        arr2.append(arr1[i])
print(len(arr2))