# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

n = int(input('введите количество долек шоколадки в длину: '))
m = int(input('введите количество долек шоколадки в ширину: '))
k = int(input('введите количество желаемых долек для отделения: '))

if (k % m == 0 or k % n == 0) and k < n * m:
    print('деление возможно, приятного аппетита')
else:
    print('к сожлаению сегодня кто-то без сладкого, Вы не можете отделить такое количество долек')