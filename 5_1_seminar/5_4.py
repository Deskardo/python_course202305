# Дано натуральное число N и последовательность из N элементов.Требуется вывести эту последовательность в
# обратном порядке. Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

def rev(n):

    if n == 0:
        return ''
    num = int(input("Введите число из последовательности: "))
    return rev(n-1)+str(num)


n = int(input("Введите количество элементов: "))
print(rev(n))
