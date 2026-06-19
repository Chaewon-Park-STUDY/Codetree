A, B= map(int, input().split())

for i in range(1,A+1):
    for j in range(i,B*i+1,i):
        print(j, end= " ")
    print()