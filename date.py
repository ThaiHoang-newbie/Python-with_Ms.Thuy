n = 5
for i in range(n, 0, -1):
    s = n - i
    k = s * ' '
    print(k, end='')
    print((2 * i - 1) * '*')