n = int(input())
x1, x2 = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.

def not_intersect(a,b): #a가 이전 끝점, b가 시작점
    return a<b

store=[]

for i,elem in enumerate(x2):
    store.append((elem,i))

store.sort()


last_end = store[0][0]

num=1
for i in range(1,n):
    if not_intersect(last_end,x1[store[i][1]]):
        num+=1
        last_end=store[i][0]
print(num)