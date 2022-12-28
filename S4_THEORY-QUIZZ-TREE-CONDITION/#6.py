x=int(input())
y=int(input())
z=int(input())
if x==3:
    if y>3:
        print ("4")
    else:
        print ("3")
else:
    if y>3:
        print("2")
        if z<10:
            print("6")
        else:
            print("5") 
    else:
        print ("1")