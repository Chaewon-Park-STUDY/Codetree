n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_value=0
for i in range(n):
    for j in range(n-2):
        num=0
        for k in range(j,j+3):
            if arr[i][k]==1:
                arr[i][k]=2
                num+=1
        for a in range(n):
            for b in range(n-2):
                new=num
                if all(arr[a][m]!=2 for m in range(b,b+3)):
                    for m in range(b,b+3):
                        if arr[a][m]==1:
                            new+=1
                    max_value= max(max_value,new)
        for x in range(n):
            for y in range(n):
                if arr[x][y]==2:
                    arr[x][y]=1
                
print(max_value)