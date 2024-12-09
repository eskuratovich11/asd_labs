class Node:
    def __init__(self, str_value: str):
        self.child_1 = None
        self.child_2 = None
        self.used = False
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

    def print(self):
        if self.child_1 is None and self.child_2 is None:
            return f'{self.value}'
        else:
            return f'{self.value}({"" if self.child_1 is None else self.child_1.print()},{"" if self.child_2 is None else self.child_2.print()})'

    def delete_node(self, number):
        if self.child_1 is not None:
            if self.child_1.value != number:
                self.child_1.delete_node(number)
            else:
                self.child_1 = None
                return
        if self.child_2 is not None:
            if self.child_2.value != number:
                self.child_2.delete_node(number)
            else:
                self.child_2 = None
                return

    def add_node(self, number, nn, right):
        if self.value == number:
            if right:
                self.child_2 = Node(str(nn))
            else:
                self.child_1 = Node(str(nn))
        else:
            if self.child_1 is not None:
                self.child_1.add_node(number, nn, right)
            if self.child_2 is not None:
                self.child_2.add_node(number, nn, right)

    def find_node(self, number, stack):
        if self.value == number:
            return f'{stack}->{number}'
        v1, v2 = None, None
        if self.child_1 is not None:
            v1 = self.child_1.find_node(number, f'{stack}->{self.value}')
        if self.child_2 is not None:
            v2 = self.child_2.find_node(number, f'{stack}->{self.value}')
        if v1 is not None:
            return v1
        elif v2 is not None:
            return v2
        return None


n = Node("8(3(1,6(4,7)),10(,14(13,)))")
while True:
    c = input("del add find exit?:")
    if c == "del":
        v = int(input("node number:"))
        if v == n.value:
            print("Критическая ошибка, удалён корневой узел")
            exit(-1)
            break
        n.delete_node(v)
    elif c == "add":
        v = int(input("node number:"))
        vn = int(input("new node number:"))
        rl = input("right or left:") == "right"
        n.add_node(v, vn, rl)
    elif c == "find":
        v = int(input("node number:"))
        print(n.find_node(v, ""))
    elif c == "exit":
        print(n.print())
        break