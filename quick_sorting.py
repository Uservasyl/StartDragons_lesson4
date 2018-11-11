import random

lst = random.sample(range(1, 100), 15)
print(lst)

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
    Sorts lists of items using quick sorting algorithm (iterative method)
    '''
    stack = []
    stack.append(start)
    stack.append(end)
    while stack:
        end = stack.pop()
        start = stack.pop()
        s = split(lst, start, end)
        if s-1 > start:
            stack.append(start)
            stack.append(s-1)
        if s+1 < end:
            stack.append(s+1)
            stack.append(end)
            
quick_sort(lst, 0, len(lst)-1)
print(lst)




