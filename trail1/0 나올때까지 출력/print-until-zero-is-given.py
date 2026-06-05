arr=[]
game_on= True
while game_on:
    n= int(input())
    if n!=0:
        arr.append(n)
    else:
        game_on= False

for elem in arr:
    print(elem)
