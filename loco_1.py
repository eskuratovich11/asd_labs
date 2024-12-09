stack = []
l = input("Введите строку: ")
m = {
    "(": ")",
    "[": "]",
    "{": "}"
}
good = "Строка существует"
bad = "Строка не существует"
for i in l:
    if i in m.keys():
        stack.append(i)
    else:
        if len(stack) == 0:
            print(bad)
            break
        if m[stack[-1]] == i:
            del stack[-1]
            continue
        else:
            print(bad)
            break
else:
    print(good if len(stack) == 0 else bad)