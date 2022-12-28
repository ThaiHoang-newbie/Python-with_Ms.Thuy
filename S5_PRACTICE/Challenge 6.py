score=int(input())
if score < 50:
    print("Bad!")
elif score >= 50 and score < 80:
    print("not bad, not good")
elif score >= 80 and score < 100:
    print("excellent")
else:
    print("Bad!")