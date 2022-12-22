def xemluong(n): 
    list = []
    a = 0
    for i in range(n):
        m = int(input("Nhập lương thành viên "+str(i + 1) +":"))
        list.append(m)
    for i in range(len(list)-1):
            for j in range(i + 1, len(list)):
                if list[i] > list[j]:
                    a = list[i]
                    list[i] = list[j]
                    list[j] = a
    return list
n = int(input("Nhập số người:"))
print(xemluong(n))