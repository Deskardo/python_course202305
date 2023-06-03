def quick_sort(array):          # алгоритм быстрой сортировки списка в рекурсии
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
print(quick_sort([14, 5, 9, 6, 3, 48, 7, 5, 2, 7]))
    
