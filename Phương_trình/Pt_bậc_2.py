from cmath import sqrt
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
while a == 0:
    if b == 0:
            print("Phương trình có một nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x = 0")
        else:
            print("Phương trình có 1 nghiệm x = ", -c / b)
    a= int(input("Nhap a :"))
delta = b * b - 4 * a * c
if delta < 0:
    print("Phương trình vô nghiệm!")
elif delta == 0:
    print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
else:
    print("Phương trình có 2 nghiệm phân biệt!")
    print("x1 = ", -b - sqrt(delta) / (2 * a))
    print("x1 = ", -b - sqrt(delta) / (2 * a))