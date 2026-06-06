N= int(input())


game_is_on= True
how_many=0

num=N
while game_is_on:
    if num%2==0:
        num= num/2
        how_many+=1
        if num==1:
            game_is_on= False
            print(how_many)
    elif num%2!=0:
        if num==1:
            game_is_on= False
            print(0)
        else:
            num= 3*num+1
            how_many+=1
            if num==1:
                game_is_on= False
                print(how_many)
