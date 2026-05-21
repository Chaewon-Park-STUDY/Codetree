
C,N= map(str, input().split())
N= int(N)


if C == "A":
    for num in range(1,N+1):
        print(num, end = " ")
else:
    for num in range(N,0,-1):
        print(num, end= " ")