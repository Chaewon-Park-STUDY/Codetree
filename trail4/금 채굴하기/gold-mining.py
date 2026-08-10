n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
#K=n-1까지

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
#아하 로직이 잘못됨

store=[]
for k in range(1,2*n-1):
    cost=k**2+(k+1)**2
    for i in range(n):
        for j in range(n):
            num_gold=0
            x,y=i,j
            for p in range(k,0,-1):
                for a in range(j-(k-p),j+(k-p+1)):
                    if in_range(i-p,a) and grid[i-p][a]==1:
                        num_gold+=1
            for p in range(j-k,j+k+1):
                if in_range(i,p) and grid[i][p]==1:
                    num_gold+=1
            for p in range(1,k+1):
                for a in range(j-(k-p),j+(k-p+1)):
                    if in_range(i+p,a) and grid[i+p][a]==1:
                        num_gold+=1

            if cost<=m*num_gold:
                store.append((num_gold))

catch=0
for elem in grid:
    for _ in elem:
        if _==1:
            catch+=1
            break
if len(store)==0 and catch!=0:
    print(1)
elif len(store)==0 and catch==0:
    print(0)
else:
    print(max(store))