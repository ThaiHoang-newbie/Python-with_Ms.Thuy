x=int(input())
y=int(input())
z=int(input())
if x==3:
    if y<3:
        print("3")
else:
    if y>3:
        if z>10:
            print("4")
    else:
        print ("1")
#bài này em thấy lỗi chỗ if, nếu đúng thì nó không làm gì cả, nhưng mà sai thì nó lại in ra chuỗi....Nên em đổi ngược lại điều kiện. Ví dụ y>3 sai, em đổi lại thành y<3 đúng