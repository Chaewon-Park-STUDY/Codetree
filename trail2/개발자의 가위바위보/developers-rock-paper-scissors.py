N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)

# Please write your code here.
store=[]

for i in range(N):
    if a[i]!=b[i]:
        store.append((a[i],b[i]))

# 규칙성을 알아냈따!
# 짝꿍 찾기
#(1,3) (2,1)(3,2) 짝꿍
first_group=[(1,2),(2,3),(3,1)]

max_val=0
num1=0
num2=0
for elem in store:
    if elem in first_group:
        num1+=1
        max_val=max(max_val,num1)
    else:
        num2+=1
        max_val=max(max_val,num2)
print(max_val)


