chieuDaiCanh = int(input())
n = ""
for i in range(chieuDaiCanh):
    n = n + "*"
print(n)
for i in range(chieuDaiCanh):
    n = n[:-1]
    print(n)