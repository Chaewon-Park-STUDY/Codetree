
N= int(input())

cnt=9

for i in range(N):
    for j in range(N):
        print(cnt, end="")
        cnt-=1
        if cnt<1:
            cnt=9
    print()