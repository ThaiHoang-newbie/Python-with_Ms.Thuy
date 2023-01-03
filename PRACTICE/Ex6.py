n=int(input())
x=""
for i in range (n):
    x=x+"X"
print(x)
n=n-1
for i in range (n):
    x=x[:-1]
    print(x)