# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
'''
arr = [1, 2, 3, 5, 8, 15, 23, 38]
result = []

for i in range(len(arr)):
    if arr[i]%2 == 0:
        result.append(f'{arr[i]}, {arr[i]**2}') # решение через строку, значения будут выведены в качестве строк

print(result)

'''

'''
arr = [1, 2, 3, 5, 8, 15, 23, 38]
result = list()

for i in arr:
    if i%2 == 0:
        result.append((i, i**2)) # решение через создание кортежа

print(result)

'''


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


arr = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, arr)
print(res)
res = where(lambda x: x % 2 == 0, arr)
print(res)
res = list(select(lambda x: (x, x**2), res)) # пример решения через lambda функцию.
print(res)