import re

#line = input("Введіть стрічку: \n")
line = 'Hello, my name is Taras. yes, yes, Taras. Taras has 5 letters!'
def sort_list(line):
    lines = re.sub('[.!,@#$]', '', line)
    lst = lines.split(' ')
    lst.sort()
    arr = []
    for i in lst:
        k = {i : lst.count(i)}
        arr.append(k)
        if arr.count(k) > 1:
            arr.remove(k)
    print(arr)



sort_list(line)