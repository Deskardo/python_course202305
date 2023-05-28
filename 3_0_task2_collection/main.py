# list_1 = [] # создание пустого списка
# list_1 = list() # создание пустого списка
# list_1 = [1, 2, 3, 4, 5, 6]
# print(*list_1) # * убирает скобки и запятые из списка и выводит последовательно все его элементы

# for i in list_1: # последовательный вовод элементов массива циклом for
#     print(i)

# print(len(list_1)) # вывести длину списка (количество элементов)
# print(list_1[0]) # вывести первый элемент списка, при указании отрицательных значений -1 и ниже будет выводится обратный порядок списка.

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # добавление элемента в конец списка.
# print(list_1)

# list_1 = []
# for i in range(5):    # Последовательное наполнение списка с помощью for
#     list_1.append(i)
# print(list_1)

# list_1.pop() # удаление последнего элемента списка

# Удаление конкретного элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12 при указании индекса, удаляется конкретный элемент списка
# print(list_1)

# Добавление элмента в список на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11)) # размещение на индекс 2(третья позиция) числа 11
# print(list_1)

# print(list_1[2:9]) # Вывести все элементы списка с индексом от 2 до 9
# print(list_1[0:len(list_1):6]) # Вывести все элементы списка с позиции 0 до позиции (длина списка) с шагом 6

# -------------------------------------------------------

# работа с кортежами
# t = ()

# print(type(t)) # команда для определения типа данных

# t = (1, )

# print(type(t)) # tuple является типом данных кортеж в конце кортежа обязательно должна быть запятая.

# v = [1, 2, 5]
# print(v)
# print(type(v))
# # преобразование класса список в класс кортеж
# v = tuple(v)
# print(v)
# print(type(v))

# # a = 1
# # b = 2         # в python можно присваивать переменные через запятую
# # a, b = 1, 2

# # a = b = 1    # при таком присвоении, двум переменным присваивается значение 1

# a, b, c = v

# print(a,b,c)

# t = (1, 2, 3, 4)

# print(t[1]) # выводит элемент кортежа с индексом 1


# --------------------------------------------------------------

# Работа со словарями

# d = {} # словари вносятся в фигурные скобочки
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d['q'])

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента

# for item in dictionary:         # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
#     print(item)


# --------------------------------------------------------------

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray') # добавить значение в множество
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # удалить элемент множества
# print(colors) # {'green', 'blue','gray'}
# colors.discard('red') # проверить если значение есть в множесте - удалить его, если нет, то ничего не делать
# colors.clear() # удалить все значения в множестве

# Операции со множествами в Python:


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} копирование множества в новое множество
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединение множеств
# i = a.intersection(b) # i = {8, 2, 5} найти пересечение
# dl = a.difference(b) # dl = {1, 3}    найти различия а от b
# dr = b.difference(a) # dr = {13, 21}  найти отличия b от а
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13} объединение -> разность с пересечением множеств

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})


#-----------------------------------------------------------

# 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]
# 1. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

# Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
# Решение:
# 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)

# print(list_1) # [1, 2, 3,..., 100]
# # Эту же функцию можно записать так:

# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# # 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]
# # Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
# # Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]
