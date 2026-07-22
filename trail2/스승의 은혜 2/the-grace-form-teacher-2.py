N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

# Please write your code here.



max_num=0
for i in range(N):
    P.sort()
    P[i]//=2
    total_sum=0
    num=0
    for j in range(N):
        if total_sum<=B:
            total_sum+=P[j]
            if total_sum<=B:
                num+=1
            else:
                total_sum-=P[j]
    P[i]*=2
    max_num= max(max_num,num)
print(max_num)