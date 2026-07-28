n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
num_A=0
num_B=0
time_A=[0 for _ in range(1000000)]
time_B= [0 for _ in range(1000000)]

start_A=0
for i in range(n):
    for j in range(t[i]):
        num_A+=1
        start_A+=v[i]
        time_A[num_A]=start_A

start_B=0
for i in range(m):
    for j in range(t2[i]):
        num_B+=1
        start_B+=v2[i]
        time_B[num_B]=start_B

total=sum(t)


num=0
rank_A=1
rank_B=1
store_A=[]
store_B=[]
for i in range(total+1):
    if time_A[i]==time_B[i]:
        rank_A,rank_B=1,1
    elif time_A[i]<time_B[i]:
        rank_A,rank_B=0,1
    elif time_A[i]>time_B[i]:
        rank_A,rank_B=1,0
    store_A.append(rank_A)
    store_B.append(rank_B)

for i in range(1,len(store_A)-1):
    if store_A[i]!=store_A[i+1]:
        num+=1
print(num)