# За день машина проезжает n километров. Сколько дней нужно, 
# чтобы проехать маршрут длиной m километров? При решении задачи
# нельзя пользоваться условной инструкцией if и циклами

n = 700
m = 750
d = int(m//n) + bool(m%n)


print(f"Чтоб проехать {m} километров, машине потребуется {d} дня(ей)")