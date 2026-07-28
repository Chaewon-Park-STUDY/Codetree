N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

time_A=[0 for _ in range(1000000)]
time_B=[0 for _ in range(1000000)]
num_A=0
num_B=0
start_A=0
start_B=0
total= sum(t)

for i in range(N):
    for j in range(t[i]):
        num_A+=1
        start_A+=v[i]
        time_A[num_A]=start_A

for i in range(M):
    for j in range(t2[i]):
        num_B+=1
        start_B+=v2[i]
        time_B[num_B]=start_B

rank_A=1
rank_B=1
store=[]

for i in range(total+1):
    if time_A[i]==time_B[i]:
        rank_A,rank_B=1,1
    elif time_A[i]>time_B[i]:
        rank_A,rank_B=1,0
    else:
        rank_A,rank_B=0,1
    store.append((rank_A,rank_B))

num=0

for k in range(len(store)-1):
    if store[k]!=store[k+1]:
        num+=1
print(num)