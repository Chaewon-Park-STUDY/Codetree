N= int(input())
game_is_on= True
cnt=0

while game_is_on:
    if N%2==0:
        N= N*3+1
        cnt+=1
        if N>=1000:
            game_is_on= False
            print(cnt)
    else:
        N= N*2+2
        cnt+=1
        if N>=1000:
            game_is_on= False
            print(cnt)