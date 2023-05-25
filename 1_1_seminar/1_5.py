# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

i = int(input('Введите номер вагона от головы поезда: '))
j = int(input('Введите текущий номер вагона: '))
result = 0

if i != j:
    result = i + j - 1
    print(result)
else:
    print("без дополнительной информации посчитать количество вагонов невозможно")