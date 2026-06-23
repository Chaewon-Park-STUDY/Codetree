n = int(input())

# Please write your code here.

cnt=1

def square(N):
    for i in range(N):
        for j in range(N):
            global cnt
            print(cnt, end=" ")
            cnt+=1
            if cnt>9:
                cnt=1
        print()
square(n)
