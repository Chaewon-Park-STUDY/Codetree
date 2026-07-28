
N= int(input())


for i in range(1,N+1):
    for j in range(1+(i-1)*i//2,1+(i-1)*i//2+i):
        print(j, end=" ")
    print()