import random

arr = [random.randint(0,1000) for i in range(1000)]


def mySort(arr):
    n = len(arr)
    swapped = False
    step = n
    while step > 1 or swapped:
        if step > 1:
            step = int(step / 1.25)
        i = 0
        swapped = False
        while i + step < n:
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
                swapped = True
            i += step


mySort(arr)
print(arr)
