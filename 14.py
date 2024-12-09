def hashfunc(s):
    h = 0
    for i in s:
        h += ord(i) - 96
    return h


with open("text.txt", "r") as file:
    f = list(set(x for x in file.read().split()))

m = [[]] * (max([hashfunc(s) for s in f]) + 1)
for i in f:
    h = hashfunc(i)
    m[h] = m[h] + [i]
with open("14_output.txt", "w") as file:
    for key, value in enumerate(m[1::]):
        file.write(f'{key + 1} : {value}\n')
