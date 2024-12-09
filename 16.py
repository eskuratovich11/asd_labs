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


n = Node("8(3(1,6(4,7)),10(,14(13,)))")
stack = []
current = n
while current is not None or len(stack)>0:
    while current is not None:
        stack.append(current)
        print(current.value,end=" ")
        current = current.child_1
    current = stack[-1]
    current = current.child_2
    del stack[-1]