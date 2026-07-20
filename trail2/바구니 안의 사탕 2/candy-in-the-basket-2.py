N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
max_value=0
for i in range(max(pos)+1):
    num=0
    for j in range(i,i+2*K+1):
        for k in range(N):
            if j==pos[k]:
                num+=candy[k]
    max_value=max(max_value,num)
print(max_value)
