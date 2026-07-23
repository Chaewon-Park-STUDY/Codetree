n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

start=0
store=[]
for i in range(n):
    if dir[i]=="R":
        start+=x[i]
    else:
        start-=x[i]
    store.append(start)

new_start=-min(store)

pos=[0 for _ in range(1001)] #각 (0,1) (1,2) , (2,3)을 의미
for i in range(n):
    if dir[i]=="R":
        for j in range(new_start,new_start+x[i]):
            pos[j]+=1
        new_start+=x[i]
    else:
        for j in range(new_start-1,new_start-x[i]-1,-1):
            pos[j]+=1
        new_start-=x[i]

num=0
for elem in pos:
    if elem>=2:
        num+=1
print(num)