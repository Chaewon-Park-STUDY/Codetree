N= int(input())
cnt=1

for i in range(N):
    for k in range(i):
        print(" ", end=" ")
    for j in range(N-i):
        print(cnt, end=" ")
        cnt+=1
        if cnt>9:
            cnt=1
    print()