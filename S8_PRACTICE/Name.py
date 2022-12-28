name=input()
word=name.split()
print(len(word))
firstname=word[0]
print ("firstname:", firstname)
if len(word)>=3:
    print("midname: ",end="")
    for x in range (len(word)-2):
        x=x+1
        midname=word[x]
        print(midname,end=" ")
    print()
lastname=word[-1]
print("lastname:",lastname)