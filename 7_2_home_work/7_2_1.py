# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.


# Ввод:                                      Вывод:
# values = [0, 2, 10, 6]                      same
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

def same_by(characteristic, items):
    if len(items) == 0:               # Проверка длины списка, если пустой, возвращаем True
        return True
    else:
        first_value = characteristic(items[0])  # Присвоить переменной значение функции от первого значения списка
    for i in items:
        if characteristic(i) != first_value:    # Проверить соответствие функции от каждого элемента списка с переменной
            return False
    return True    


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')