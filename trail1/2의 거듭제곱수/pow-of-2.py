N= int(input())


num= N
game_is_on= True
how_many=0

while game_is_on:
    num=num/2
    how_many+=1
    if num==1:
        game_is_on= False
        print(how_many)