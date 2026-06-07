arr=input()
N= int(input())

if N<=len(arr):
    for i in range(-1,-1-(N) ,-1):
        print(arr[i], end= "")
else:
    for i in range(-1,-len(arr)-1,-1):
        print(arr[i], end="")
