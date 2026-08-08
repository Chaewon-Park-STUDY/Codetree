n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]



#내 코드의 문제점
# 1 1 1 
# 1 1 0 일때 가로축 기준으로 하면 캐치 못함

# Please write your code here.

arr=[
    [0 for _ in range(m)]
    for _ in range(n)
]


for i in range(n):
    for j in range(m):
        if grid[i][j]>0:
            arr[i][j]=1
        else:
            arr[i][j]=0

store=[]
for i in range(n):
    for j in range(m):
        min_val_col=1000
        min_val_row=1000
        if arr[i][j]==1:
            num=0
            for p in range(i,n):
                if arr[p][j]==1:
                    num+=1
                    for l in range(j+1,m):
                            if arr[p][l]==1:
                                continue
                            else:
                                min_val_row=min(min_val_row,l-j)
                                break
                
                    if min_val_row==1000:
                        min_val_row=m-j
                    store.append(min_val_row*num)
                else:
                    break
            #min_val_col=min(min_val_col,num)
        else:
            num=0
               
        store.append((min_val_row*num))

if len(store)==0 or max(store)==0:
    print(-1)
else:
    print(max(store))

