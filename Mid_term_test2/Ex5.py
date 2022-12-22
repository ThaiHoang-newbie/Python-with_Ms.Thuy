
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




    