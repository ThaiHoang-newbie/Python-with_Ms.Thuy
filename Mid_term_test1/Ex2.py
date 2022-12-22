kiemtra=True
S=0
while kiemtra:
    n=int(input("Hãy nhập số: "))
    if n>0:
        kiemtra= False
text=""
for i in range (1,n+1):
    S=S+i
    text=text+str(i)+"+"
print("Tổng S là: ",text[:-1],"=",S)