N= int(input())

for i in range(N):
    arr=[]
    for j in range(N):
        arr.append(j+1)
    if i%2!=0:
        arr.reverse()

    for elem in arr:
        print(elem,end="")   
    print()