def tinhluong(gioLam,luongGio):
    a = 0
    b = 0
    x = 1
    if gioLam <= 40:
        return x * gioLam * luongGio
    if gioLam > 40:
        a = 40 * luongGio
        b = (gioLam - 40) * (luongGio * 1 + luongGio/2)
        return x * (a + b)
gioLam = float(input("Nhập số giờ làm:"))
luongGio = float(input("Nhập số lương giờ:"))
print(tinhluong(gioLam,luongGio))