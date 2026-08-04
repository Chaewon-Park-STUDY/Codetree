
a=int(input())

if a==25:
    print("Good")
while a!=25:
    if a<25:
        print("Higher")
    elif a>25:
        print("Lower")
    a=int(input())
    if a==25:
        print("Good")
        break