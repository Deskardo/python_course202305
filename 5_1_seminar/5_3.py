# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

n = int(input())

def prime_num(n):
    count = 0
    for i in range(n):
        if i > 0 and n%i == 0:
            count +=1
    if count == 1:
        print('yes')
    else:
        print('no')
            
prime_num(n)