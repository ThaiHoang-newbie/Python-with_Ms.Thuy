def containsOneA(string):
    x = 0
    for i in string:
        if i == "a":
            x = x + 1
            break
    if x == 0:
        check = False
    else:
        check = True
    return check
print(containsOneA("b"))
if containsOneA(input("nhập chuỗi:")) == True:
    print("Chuỗi này có kí tự a")
else:
    print("Chuỗi này không có kí tự a")