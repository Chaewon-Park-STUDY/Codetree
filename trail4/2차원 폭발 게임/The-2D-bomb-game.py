n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.



trial=0

def clock(arr):
    new=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[j][n-1-i]=arr[i][j]
    return new
import copy

while trial<k:
    trial+=1
    while True:
        changed=False
        for i in range(n):
            for j in range(n-1):
                if grid[j][i]!=0:
                    for l in range(j+1,n):
                        if grid[j][i]==grid[l][i]:
                            if l==n-1 and l-j+1>=m:
                                for q in range(j,l+1):
                                    grid[q][i]=0
                                changed=True
                            else:
                                continue
                        else:
                            if l==n-1 and m==1:
                                grid[l][i]=0
                                changed=True
                            if l-j>=m:
                                for q in range(j,l):
                                    grid[q][i]=0
                                changed=True
                            break
            num=0
            store=[]
            for j in range(n):
                if grid[j][i]==0:
                    num+=1
                else:
                    store.append(grid[j][i])
            for j in range(num,n):
                grid[j][i]=store[j-num]
            for j in range(0,num):
                grid[j][i]=0
    #여기까지가 한번 폭탄이 떨어지고 난 후의 상ㅇ황
        if not changed:
            break
    grid=clock(grid)
    for i in range(n):
        num=0
        store=[]
        for j in range(n):
            if grid[j][i]==0:
                num+=1
            else:
                store.append(grid[j][i])
        for j in range(num,n):
            grid[j][i]=store[j-num]
        for j in range(0,num):
            grid[j][i]=0

    while True:
        changed=False
        for i in range(n):
            for j in range(n-1):
                if grid[j][i]!=0:
                    for l in range(j+1,n):
                        if grid[j][i]==grid[l][i]:
                            if l==n-1 and l-j+1>=m:
                                for q in range(j,l+1):
                                    grid[q][i]=0
                                changed=True
                            else:
                                continue
                        else:
                            if l==n-1 and m==1:
                                grid[l][i]=0
                                changed=True
                            if l-j>=m:
                                for q in range(j,l):
                                    grid[q][i]=0
                                changed=True
                            break
            num=0
            store=[]
            for j in range(n):
                if grid[j][i]==0:
                    num+=1
                else:
                    store.append(grid[j][i])
            for j in range(num,n):
                grid[j][i]=store[j-num]
            for j in range(0,num):
                grid[j][i]=0
        if not changed:
            break

    
   
    if trial==k:
        break

sum_val=0
for elem in grid:
    for _ in elem:
        if _!=0:
            sum_val+=1

if n!=1:
    print(sum_val)
else:
    if m>1:
        print(n)
    else:
        print(0)

