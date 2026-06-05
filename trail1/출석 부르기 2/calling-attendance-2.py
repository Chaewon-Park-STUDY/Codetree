game_is_on= True

while game_is_on:
    n= int(input())
    if n==1:
        print("John")
    elif n==2:
        print("Tom")
    elif n==3:
        print("Paul")
    elif n==4:
        print("Sam")
    else:
        game_is_on= False
        print("Vacancy")