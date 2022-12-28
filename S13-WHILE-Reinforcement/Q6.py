a = 0
while a < 3:
    b = int(input())
    if b > 5 and b < 10:
        print("You Won!")
        break
    else:
        a = a + 1
if a == 3:
    print("Game over")