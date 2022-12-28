text = input()
m = len(text)
n = m/2
n = round(n - 0.5)
a = text[:n]
n = n + 1
b = text[n:]
x=""
for i in b:
    x = i + x
if a == x:
    print("It is symmetric word")
else:
    print("It isn't symmetric word")