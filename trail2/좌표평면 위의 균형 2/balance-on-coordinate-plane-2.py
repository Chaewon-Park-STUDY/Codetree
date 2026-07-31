n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

min_x=100
max_x=0
min_y=100
max_y=0

for elem in points:
    if elem[0]<=min_x:
        min_x=elem[0]
    if elem[0]>=max_x:
        max_x=elem[0]
    if elem[1]<=min_y:
        min_y=elem[1]
    if elem[1]>=max_y:
        max_y=elem[1]

a=max_x
b=max_y

arr=[
    [0 for _ in range(b+1)]
    for _ in range(a+1)
]

for i in range(a+1):
    for j in range(b+1):
        for elem in points:
            if elem[0]==i and elem[1]==j:
                arr[i][j]=1

store=[]

for i in range(0,a+1,2):
    for j in range(0,b+1,2):
        num=0
        max_val=0
        for m in range(b+1):
            arr[i][m]="L"
        for k in range(a+1):
            arr[k][j]="L" 
        for c in range(0,i):
            for d in range(0,j):
                if arr[c][d]==1:
                    num+=1
        max_val=max(max_val,num)
        num=0
        for e in range(0,i):
            for f in range(j,b+1):
                if arr[e][f]==1:
                    num+=1
        max_val=max(max_val,num)
        num=0
        for g in range(i,a+1):
            for h in range(0,j):
                if arr[g][h]==1:
                    num+=1
        max_val=max(max_val,num)
        num=0
        for q in range(i,a+1):
            for p in range(j,b+1):
                if arr[q][p]==1:
                    num+=1
        max_val=max(max_val,num)
    
        store.append(max_val)
        
        for m in range(b+1):
            arr[i][m]=0
        for k in range(a+1):
            arr[k][j]=0

print(min(store))