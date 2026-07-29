N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

# Please write your code here.

store=[]

for i in range(N):
    store.append((pigeon[i],position[i]))

arr=[0 for _ in range(11)] #1 index는 1번 비둘기의 원래 위치, 시작포인트


new=[]
for i in range(N):
    if store[i][0] not in new:
        new.append(store[i][0])
        arr[store[i][0]]= store[i][1]



total=0
for i in range(len(store)):
    for j in range(1,11):
        if store[i][0]==j and store[i][1]!=arr[j]:
            if store[i][1]==0:
                arr[j]=0
                total+=1
            else:
                arr[j]=1
                total+=1
print(total)





