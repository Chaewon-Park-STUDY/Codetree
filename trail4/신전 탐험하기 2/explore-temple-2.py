n = int(input())
l, m, r = [], [], []

for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.
grid=[[0 for _ in range(3)] for _ in range(n)]
choice = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(n)]

for i in range(n):
    grid[i][0]=l[i]
    grid[i][1]=m[i]
    grid[i][2]=r[i]

for s in range(3):
    choice[0][s][s] = grid[0][s]

for i in range(1, n):
    for j in range(3):        
        for k in range(3): 
            max_val=0
            if i!=n-1:
                for prev in range(3):  
                    if prev != j:
                        max_val=max(max_val,choice[i-1][prev][k])
            else:
                for prev in range(3):  
                    if prev != j  and k!=j:
                         max_val=max(max_val,choice[i-1][prev][k])
            if max_val>0:
                choice[i][j][k]=max_val+grid[i][j]
maximum=0

for elem in choice[n-1]:
    for _ in elem:
        maximum=max(maximum,_)
print(maximum)
