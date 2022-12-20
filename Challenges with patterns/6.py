chieuDaiCanh = int(input())
n = ""
for i in range(chieuDaiCanh):
    n = n + "*"
    print(n)
m = ""
for i in range(chieuDaiCanh):
    m = m + "*"
for i in range(chieuDaiCanh):  
    m = m[:-1]
    print(m)