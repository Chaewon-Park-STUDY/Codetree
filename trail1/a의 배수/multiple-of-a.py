
N, a= map(int, input().split())

i=1

while 1<=i<=N:
    if i%a==0:
        print(1)
        i+=1
    else:
        print(0)
        i+=1