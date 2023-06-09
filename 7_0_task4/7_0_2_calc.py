'''

def calc1(a):
    return a+a

def calc2(a):
    return a*a

def math(op, x):   # функция может принимать в качестве аргумента другую функцию
    print(op(x))
    
math(calc2, 5)

'''

def calc2(a, b):
    return a*b

def math(op, x, y):   # функция может принимать в качестве аргумента другую функцию
    print(op(x, y))
    
calc1 = lambda a, b: a + b # пример lambda функции, которая позволяет сократить количество кода и оптимизировать программу
    
math(calc1, 5, 45)   # math(lambda a, b: a + b, 5, 45) можно сразу предавть в качестве одной из переменных lambda функцию, дополнительно уменьшая объём кода.