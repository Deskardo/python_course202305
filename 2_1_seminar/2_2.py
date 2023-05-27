# дано натуральное число А > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что  φ(n)=A. Если А не является числом Фибоначчи выведите число -1.

a = int(input('Введите натуральное число больше 1:'))
a1 = 0
a2 = 1
result = 1
count = 2

while a > result:
    result = a1 + a2
    a1 = a2
    a2 = result
    count += 1
if a == result:
    print(f'{a} является {count}-м числом Фибоначчи')
else:
    print('-1')