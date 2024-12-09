import random

arr = [random.randint(0, 1000) for i in range(1000)]


def mySort(arr):
    max_digits = max([len(str(x)) for x in arr])

    carr = arr.copy()
    for i in range(0, max_digits):
        bins = [[] for _ in range(10)]
        for x in carr:
            digit = (x // 10 ** i) % 10
            bins[digit].append(x)
        carr = [x for queue in bins for x in queue]
    arr.clear()
    arr += carr


mySort(arr)
print(arr)
