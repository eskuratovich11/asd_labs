import random

arr = [random.randint(0, 1000) for i in range(1000)]


def mySort(arr):
    if len(arr) <= 1:
        return arr
    left = mySort(arr[:len(arr) // 2])
    right = mySort(arr[len(arr) // 2:])
    n = m = k = 0
    sarr = [0] * len(arr)
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            sarr[k] = left[n]
            n += 1
        else:
            sarr[k] = right[m]
            m += 1
        k += 1
    while n < len(left):
        sarr[k] = left[n]
        n += 1
        k += 1
    while m < len(right):
        sarr[k] = right[m]
        m += 1
        k += 1
    for i in range(len(arr)):
        arr[i] = sarr[i]
    return arr


print(mySort(arr))
#?