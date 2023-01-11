text = input()
index=""
for i in range(len(text)):
    if text[i] == "a":
        index = index + str(i)+","
if index == "":
    print("a not found")
else:
    print("a found at the index of", index[:-1])