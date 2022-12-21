def getIndexOf(string):
    for i in range(len(string)):
        if string[i] == ";":
            return i
def getLastName(string,vitri):
    return string[:vitri]
def getFirstName(string,vitri):
    return string[1+vitri:]
string = input("Nhap ho;ten :")
vitri= getIndexOf(string)
print("first name is :",getFirstName(string,vitri))
print("Last name is :",getLastName(string,vitri))