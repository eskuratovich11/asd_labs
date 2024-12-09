def div(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y


opers = [
    {
        "*": lambda x, y: x * y,
        "/": div
    },
    {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y
    }
]


def solve(eq) -> int:
    depth = []
    solved = []
    for key, value in enumerate(eq):
        if value == "(":
            depth.append(key)
        elif value == ")":
            if len(depth) == 1:
                substr = eq[depth[0] + 1:key]
                solved.append(("(" + substr + ")", solve(substr)))
            del depth[-1]
    if len(depth) != 0:
        raise Exception
    for v1, v2 in solved:
        eq = eq.replace(v1, str(v2), 1)
    sp = ["*", "/", "+", "-"]
    vals = []
    ops = []
    start = 0
    for key, value in enumerate(eq):
        if value in sp:
            ops.append(value)
            vals.append(int(eq[start:key]))
            start = key + 1
    vals.append(int(eq[start:]))
    for i in opers:
        key_1 = 0
        while key_1 != len(ops):
            op = ops[key_1]
            if op in i.keys():
                vals[key_1] = i[op](vals[key_1], vals[key_1 + 1])
                del vals[key_1 + 1]
                del ops[key_1]
            else:
                key_1 += 1

    return vals[0]


s = input()[:-1:]
try:
    print(solve(s))
except ZeroDivisionError as e:
    print("На ноль делить нельзя")
except Exception as e:
    print(e.with_traceback())
    print("Скобки стоят неправильно")
