n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

store=[]
increase=[1 for _ in range(n)]
decrease=[1 for _ in range(n)]


for i in range(1,n):
    for j in range(i):
        if sequence[i]>sequence[j]:
            increase[i]=max(increase[i],increase[j]+1)

for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if sequence[i]>sequence[j]:
            decrease[i]=max(decrease[i],decrease[j]+1)

store.append(max(increase))
store.append(max(decrease))



for i in range(n):
        store.append(increase[i]+decrease[i]-1)
print(max(store))