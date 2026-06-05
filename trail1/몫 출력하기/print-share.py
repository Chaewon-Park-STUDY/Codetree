game_is_on = True
num=0
while game_is_on:
    n= int(input())
    if n%2!=0:
        pass
    else:
        print(n//2)
        num+=1
        if num==3:
            game_is_on= False
