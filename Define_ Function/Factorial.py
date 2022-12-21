def factorial (a):
    i=1
    for k in range (a):
        i=i*(k+1)
    return i
n=int(input())
print(factorial(n))