width = int(input())
height= int(input())
a = ""
b = ""
for i in range(width):
    n = i + 1
    a = n * "x"
    b = b + a + " "
for i in range(height):
    print(b)