
N= int(input())

cnt=65
for i in range(N):
    for j in range(i):
        print(" ", end=" ")
    for j in range(N-i):
        print(chr(cnt), end=" ")
        cnt+=1
        if ord(chr(cnt))> ord("Z"):
            cnt=65
    print()
