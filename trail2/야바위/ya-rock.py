n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.
# 번호를 바꾸는게 아니고 해당 위치 번호에 있는 종이컵을 교환하는 식으로

arr=[0 for _ in range(n+1)]

store=[]
for i in range(1,4):
    score=0
    arr[i]=1
    obj=i
    for j in range(n):
        if a[j]==obj:
            obj=b[j]
        elif b[j]==obj:
            obj=a[j]
        if obj==c[j]:
            score+=1
    arr[i]=0
    store.append((score,i))

max_score=0

for x,y in store:
    if x>=max_score:
        max_score=x
print(max_score)