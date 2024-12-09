import random

arr = [random.randint(0, 1000) for i in range(1000)]


def mySort(arr):
    for j in range(2, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key


mySort(arr)
print(arr)
