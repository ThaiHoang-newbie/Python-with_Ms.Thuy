width = int(input())
height= int(input())
a = ""
b = ""
for n in range(width):
    a = width * "x"
    b = b + a + " "
    width = width - 1
for i in range(height):
    print(b)