A,B= map(int, input().split())

C= B-A

for i in range(1,5):
    for j in range(C+1):
        print(f"{B-j} * {2*i} = {(B-j)*2*i}", end=" ")
        if j < C: 
            print("/", end=" ")
    print()
