x = int(input())
a = ""
b = ""
for n in range(x):
    a = x * "x"
    b = b + a + " "
    x = x - 1
print(b) 