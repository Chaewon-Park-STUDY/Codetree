n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import copy
dxs,dys=[-1,0,1,0],[0,1,0,-1] # 순서대로 북, 동, 남, 서

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

max_val=0
for i in range(n):
    for j in range(n):
        num=0
        arr=copy.deepcopy(grid)
        start=arr[i][j]
        for k in range(1,start):
            if in_range(i-k,j):
                arr[i-k][j]=0
            if in_range(i,j+k):
                arr[i][j+k]=0
            if in_range(i+k,j):
                arr[i+k][j]=0
            if in_range(i,j-k):
                arr[i][j-k]=0
        arr[i][j]=0
        for k in range(n):#열별
            count_num=0
            for a in range(0,n):
                if arr[a][k]==0:
                    count_num+=1
            new=[]
            for a in range(0,n):
                if arr[a][k]!=0:
                    new.append(arr[a][k])
                    arr[a][k]=0
            for b in range(count_num,count_num+len(new)):
                arr[b][k]=new[b-count_num]
      
        for a in range(n):
            for b in range(n):
                if arr[a][b]!=0:
                    x,y=a,b
                    for k in range(4):
                        dir=k
                        nx,ny=x+dxs[dir],y+dys[dir]
                        if in_range(nx,ny) and arr[nx][ny]==arr[a][b]:
                            num+=1
        max_val=max(max_val,num//2)

print(max_val)
                        
