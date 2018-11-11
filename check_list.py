import random

# lst = random.sample(range(1, 100), 15)
lst = [1,2,6,9]
def is_Sorted(lst):
    '''Повертає значення True, якщо список посортований
        і значення False в іншому випадку
    '''
    if len(lst) == 1:
        return True
    else:
        return lst[0] <= lst[1] and is_Sorted(lst[1:])

print(is_Sorted(lst))