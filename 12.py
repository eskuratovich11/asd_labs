with open("12_input.txt", "r") as f_input:
    with open("12_output.txt", "w") as f_output:
        g_min = -1
        c_min = 10 ** 10
        for _ in range(10000):
            for i in range(10000):
                n = int(f_input.readline())
                if g_min < n < c_min:
                    c_min = n
            f_output.write(str(c_min) + "\n")
            f_input.seek(0)
            g_min = c_min
            c_min = 10 ** 10
