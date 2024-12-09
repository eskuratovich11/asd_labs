class Node:
    def __init__(self, str_value: str):
        self.child_1 = None
        self.child_2 = None
        if "(" not in str_value:
            self.value = int(str_value)
            return
        else:
            self.value = int(str_value[:str_value.index("(")])
        n_index = 0
        cnt = 0
        for key, value in enumerate(str_value):
            if value == "(":
                cnt += 1
            elif value == ")":
                cnt -= 1
            elif value == "," and cnt == 1:
                n_index = key
                break
        ch_1 = str_value[str_value.index("(") + 1: n_index]
        ch_2 = str_value[n_index + 1: str_value.rindex(")")]
        if ch_1 != "":
            self.child_1 = Node(ch_1)
        if ch_2 != "":
            self.child_2 = Node(ch_2)

    def print_1(self):
        return " ".join([x for x in [str(self.value), ("" if self.child_1 is None else self.child_1.print_1()), ("" if self.child_2 is None else self.child_2.print_1())] if x != ""])
    def print_2(self):
        return " ".join([x for x in [("" if self.child_1 is None else self.child_1.print_2()),str(self.value),  ("" if self.child_2 is None else self.child_2.print_2())] if x != ""])
    def print_3(self):
        return " ".join([x for x in [("" if self.child_1 is None else self.child_1.print_3()),  ("" if self.child_2 is None else self.child_2.print_3()),str(self.value)] if x != ""])


n = Node("8(3(1,6(4,7)),10(,14(13,)))")
print(f'прямой обход : {n.print_1()}')
print(f'центральный обход : {n.print_2()}')
print(f'концевой обход : {n.print_3()}')
