def check(string):
    a = 0
    b = 0
    for i in string:
        if i == "A":
            a = a + 1
        elif i == "B":
            b = b + 1
    if a == 2 and b == 2 :
        return True
    else :
        return False
string = input("")
if check(string):
    print("Weldone")
else:
    print("lost")