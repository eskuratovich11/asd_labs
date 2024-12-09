import random

arr = [random.randint(0, 1000) for i in range(1000)]


def mySort(arr):
    for i in range(len(arr)):
        m = arr[i]
        ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < m:
                m = arr[j]
                ind = j
        arr[i], arr[ind] = arr[ind], arr[i]


mySort(arr)
print(arr)
