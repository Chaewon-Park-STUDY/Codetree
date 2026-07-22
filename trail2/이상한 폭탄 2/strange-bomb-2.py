N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

store=[]

def bomb(a,b,k):
    if b-a<=k:
        return True

for i in range(N-1):
    for j in range(i+1,N):
        if num[i]==num[j] and bomb(i,j,K):
            store.append(num[i])

if len(store)>=1:            
    print(max(store))
else:
    print(-1)



