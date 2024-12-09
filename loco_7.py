import random

arr = [random.randint(0, 1000) for i in range(1000)]


def mySort(arr):
    ind = len(arr)
    step = len(arr) // 2
    while step > 0:
        for i in range(step, ind, 1):
            j = i
            a = j - step
            while a >= 0 and arr[a] > arr[j]:
                arr[a], arr[j] = arr[j], arr[a]
                j = a
                a = j - step
        step //= 2


mySort(arr)
print(arr)
