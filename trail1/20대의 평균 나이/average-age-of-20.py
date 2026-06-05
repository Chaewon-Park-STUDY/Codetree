game_is_on= True

arr=[]
while game_is_on:
    n= float(input())
    if 0<=(n-20)<=9:
        arr.append(n)
    else:
        game_is_on= False


#print(float(round(sum(arr)/len(arr), 2)))
print(format(sum(arr)/len(arr), '.2f'))   # give 2 digits after the point
