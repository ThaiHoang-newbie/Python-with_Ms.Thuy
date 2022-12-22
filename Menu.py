while True:
    def a():
        return "MENU\nXin vui lòng chọn:\n1.Xem lịch\n2.Tính lương\n3.Xem lương\n4.Xem thông tin nhân viên\n5.Tính điểm của học sinh\n6.Thoát chương trình"
    print(a())
    choose=int(input("Lựa chọn của bạn: "))    
    if choose == 1:
        #Bài 1
        def ngay(thang):
            thang31=[1 , 3 , 5 , 7 , 8 , 10 , 12]
            while thang < 1 or thang > 12:
                thang=int(input("Nhập lại tháng: "))
            if thang == 2:
                year=int(input("nhập năm: "))
                if year %4 == 0 :
                    return "Tháng " +str(thang)+" năm " +str(year)+" có 29 ngày"
                else:
                    return "Tháng "+str(thang)+" năm " +str(year)+" có 28 ngày"
            elif thang in thang31:
                return "Tháng "+str(thang)+" có 31 ngày"
            else:
                return "Tháng "+str(thang)+" có 30 ngày"
        thang=int(input("Nhập tháng: "))
        print(ngay(thang))
    elif choose == 2:
        #Bài 2
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
        gioLam = int(input("Nhập số giờ làm:"))
        luongGio = int(input("Nhập số lương giờ:"))
        print(tinhluong(gioLam,luongGio))
    elif choose == 3:
        #Bài 3
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
        a=input("Nếu bạn muốn quay lại menu: Nhập back\nNếu bạn muốn thoát chương trình : Nhập out\n")
        if a=="back":
            continue
        elif a=="out":
            print("Cảm ơn bạn đã sử dụng!")
            break
    elif choose == 4:
        #Bài 4
        def ten():
            nhapten=input("Nhập họ và tên: ")
            a = 0
            for i in range(len(nhapten)):
                if nhapten[i] ==" ":
                    a = i
            t = str(nhapten[:a].title())
            print(t)
            """return "Họ và tên lót của nhân viên: "+str(nhapten[:a].title())+"\n"+"Tên của nhân viên: "+str(nhapten[1+a:].title())+"\n"+"Họ và tên đầy đủ của nhân viên: "+str(nhapten.title())"""
        print(ten())
        a=input("Nếu bạn muốn quay lại menu: Nhập back\nNếu bạn muốn thoát chương trình : Nhập out\n")
        if a=="back":
            continue
        elif a=="out":
            print("Cảm ơn bạn đã sử dụng!")
            break
    elif choose == 5:
        #Bài 5
        def diem():
            n = int(input("Hãy nhập số môn bạn cần tính điểm:"))
            hesototal = 0
            diemmontotal = 0
            a=""
            list=[1, 1.5, 2, 2.5, 3]
            for i in range(n):
                diemmon = float(input("Nhập điểm môn "+str(i + 1)+" :"))
            while diemmon >10 or diemmon <0:
                diemmon = int(input("Nhập lại điểm môn "+str(i + 1)+" :"))
                heso = float(input("Nhập hệ số môn "+str(i + 1)+":"))
                while heso not in list:
                    heso = float(input("Nhập lại hệ số: "))
            
                hesototal = hesototal + heso
                diemmontotal = diemmontotal + (heso * diemmon)
            diemmontotal = diemmontotal / hesototal
            a ="Tổng hệ số là: "+str(hesototal)+"\n"+"Điểm trung bình của "+str(n)+ " môn học:" + str(diemmontotal)
            return a
        print(diem())
        a=input("Nếu bạn muốn quay lại menu: Nhập back\nNếu bạn muốn thoát chương trình : Nhập out\n")
        if a=="back":
            continue
        elif a=="out":
            print("Cảm ơn bạn đã sử dụng!")
            break
    elif choose == 6:
        print("Đã thoát chương trình")
        break