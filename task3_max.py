import random
arr = [random.randint(0, 9) for lst in range(0, 5)]
print ("Input list - {}".format(arr))


def min_sum_numbers(arr):
    i = 0
    L = []
    R = []

    for i in range(len(arr)):#сортуємо список методом включення
        j = i - 1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1

    k = 0
    for k in range(0, len(arr)):# розбиваємо список на дві частини
        if k % 2 == 0:
            L.append(arr[k])
        else:
            R.append(arr[k])
    L = [str(i) for i in L]# перетворюємо числа в строку 
    R = [str(i) for i in R]
    s = ''
    L =int(s.join(L))# перетворюємо строку в ціле число 
    R =int(s.join(R))
    print("Найменшою сумою буде {}, а числами є - {} і {}".format(L+R, L, R))

min_sum_numbers(arr)