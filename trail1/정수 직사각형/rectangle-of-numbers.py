N, M= map(int, input().split())


for i in range(0, N):
    for j in range(i*M+1, (i+1)*M+1):
        print(j, end= " ")
    print()
        
