import math

x = int(input())
ans = []
for x_1 in range(int(math.log(x,3))):
    for x_2 in range(int(math.log(x, 5))):
        for x_3 in range(int(math.log(x, 7))):
            ans.append(3**x_1 * 5**x_2 * 7**x_3)
print(sorted(ans))