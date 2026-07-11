T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.
grid=[0 for _ in range(1000)]


for i in range(T):
    grid[x[i]-1]=c[i]

group_S=[0 for _ in range(1000)]
group_N=[0 for _ in range(1000)]

for _ in range(1000):
    min_val=1000
    small_val=1000
    for j in range(1000):
        if grid[j]=="S":
            min_val=min(min_val, abs(_-j))
    group_S[_]= min_val
    for k in range(1000):
        if grid[k]=="N":
            small_val=min(small_val, abs(_-k))
    group_N[_]= small_val


def get_diff(_):
    if group_S[_]<=group_N[_]:
            return True
cnt=0

for i in range(a-1,b):
    if get_diff(i):
        cnt+=1
print(cnt)
