def ngay(thang):
    thang31=[1 , 3 , 5 , 7 , 8 , 10 , 12]
    while thang < 1 or thang > 12:
        thang=int(input("Nhập lại tháng: "))
    if thang == 2:
        year=int(input("nhập năm: "))
        if year%4==0:
            return "Tháng " +str(thang)+" năm " +str(year)+" có 29 ngày"
        else:
            return "Tháng "+str(thang)+" năm " +str(year)+" có 28 ngày"
    elif thang in thang31:
        return "Tháng "+str(thang)+" có 31 ngày"
    else:
        return "Tháng "+str(thang)+" có 30 ngày"
thang=int(input("Nhập tháng: "))
print(ngay(thang))