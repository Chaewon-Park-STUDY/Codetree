game_is_on= True

while game_is_on:
    n= int(input())
    if n<25:
        print("Higher")
    elif n>25:
        print("Lower")
    else:
        game_is_on= False
        print("Good")