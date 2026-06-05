game_is_on= True

while game_is_on:
    arr=list(map(str, input().split()))
    if arr[2]!= "C":
        print(int(arr[0])* int(arr[1]))
    else:
        print(int(arr[0])* int(arr[1]))
        game_is_on= False

