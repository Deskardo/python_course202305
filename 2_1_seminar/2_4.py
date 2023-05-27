# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

n = int(input('Введите количество просматриваемых арбузов:'))

while n < 2:
    print('указанное число не может меньше двух')
    n = int(input('Введите количество просматриваемых арбузов:'))
    
arr = [i for i in range(n)] # список масс просматреваемых арбузов


for i in range(n):          # цикл для ввода масс арбузов
    arr[i] = int(input(f'введите вес {i + 1}-го арбуза: '))
    while arr[i] <= 0:
        arr[i] = int(input(f'вес арбуза не может быть ноль и меньше, введите корректный вес {i + 1}-го арбуза: '))
        
    if i == 0:
        max = arr[i]
        min = arr[i]        
    elif arr[i] > max:
        max = arr[i]
    elif arr[i] < min:
        min = arr[i]

        
print(f'Иван Васильевич купит себе арбуз на {max} кг., а теще на {min} кг.')