def countryname(a,b,c):
    x=["China", "India", "USA", "Indonesia", "Pakistan"]
    if a and b and c in x:
        return True
    else:
        return False
def population(i):
    if i=="China":
        i=4
    elif i=="India":
        i=3
    elif i=="USA":
        i=2
    elif i=="Indonesia":
        i=1
    else:
        i=0
    return i
def largest(m,n,k):
    if m>n and m>k:
        return m
    elif n>k and n>m:
        return n
    else:
        return k
country1=input("Country 1: ")
country2=input("Country 2: ")
country3=input("Country 3: ")
if countryname(country1,country2,country3):
    x=["Pakistan","Indonesia","USA","India","China"]
    print("Largest population country is: ", x[largest(population(country1),population(country2),
    population(country3))])
else:
    print("Erorr, bad country name entered")