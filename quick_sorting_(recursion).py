import random

lst = random.sample(range(1, 100), 10)
print(lst)

def split(lst, start, end):
    i = start - 1
    splitter = lst[end]
    for j in range(start, end):
        if lst[j] >= splitter:
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




