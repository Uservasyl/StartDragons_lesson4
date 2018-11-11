import random

lst = random.sample(range(1, 100), 10)

def split(lst, start, end):
    i = start - 1
    splitter = lst[end]
    for j in range(start, end):
        if lst[j] <= splitter:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[end] = lst[end], lst[i+1]
    return i+1

def quick_sort(lst, start, end):
    '''
    Sorts lists of items using quick sorting algorithm (recursion method)
    '''
    if start < end:
        s = split(lst, start, end)
        quick_sort(lst, start, s-1)
        quick_sort(lst, s+1, end)

quick_sort(lst, 0, len(lst)-1)
print(lst)

def suma_numbers():
    number = int(input("Введіть число для якого потрібно знайти суму пари чисел: \n"))
    i = 0
    MAX = 0
    while i < len(lst)-1:
        j = i + 1
        while j < len(lst)-1:
            suma = lst[i] + lst[j]
            if suma <= number and suma > MAX:
                MAX = suma
                MAXi = i
                MAXj = j
            j += 1
        i += 1
    print("Cума чисел = {}, а числами будуть {} і {}".format(MAX, lst[MAXi], lst[MAXj]))

suma_numbers()