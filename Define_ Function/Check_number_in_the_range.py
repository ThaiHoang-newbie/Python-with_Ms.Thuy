def isInteger(z):
    b=["0","1","2","3","4","5","6","7","8","9"]
    for n in z:
        if n not in b:
            return False
    return True
def isInRange(c,d,e):
    if c>d and c<e:
        return True
    else:
        return False
value=input("enter a value: ")
min=input("enter a min: ")
max=input("enter a max: ")
if isInteger(value) and isInteger(min) and isInteger(max):
    if isInRange(int(value),int(min),int(max)):
        print("Value correct")
    else:
        print(value,"is not in the range",min,max)
else:
    print("Error: value,min,max must be numbers")