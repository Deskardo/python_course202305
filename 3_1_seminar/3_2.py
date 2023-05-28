# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K - положительное число.

from random import randint

n = int(input('Введите длину масива: '))
k = int(input('Введите K для сдвига: '))
arr1 = [randint(1, 10) for i in range(n)]
arr2 = []
print(arr1)


for i in range(n):
        arr2.append(arr1[i-k%n])
print(arr2)