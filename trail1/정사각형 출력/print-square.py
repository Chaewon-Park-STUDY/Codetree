N= int(input())

for i in range(N):
    for j in range(1+N*i,N*(i+1)+1):
        print(j, end=" ")
    print()