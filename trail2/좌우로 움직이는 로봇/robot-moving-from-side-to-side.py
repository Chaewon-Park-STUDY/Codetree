n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
start_A=0
num_A=0
start_B=0
num_B=0
time_A=[0 for _ in range(2000000)]
time_B=[0 for _ in range(2000000)]
total_A=sum(t)
total_B=sum(t_b)


for i in range(n):
    if d[i]=="R":
        for j in range(t[i]):
            num_A+=1
            start_A+=1
            time_A[num_A]=start_A
    else:
        for j in range(t[i]):
            num_A+=1
            start_A-=1
            time_A[num_A]=start_A

for i in range(m):
    if d_b[i]=="R":
        for j in range(t_b[i]):
            num_B+=1
            start_B+=1
            time_B[num_B]=start_B
    else:
        for j in range(t_b[i]):
            num_B+=1
            start_B-=1
            time_B[num_B]=start_B


num=0
if total_A<=total_B:
    for k in range(2,total_A+1):
        if time_A[k-1]!=time_B[k-1] and time_A[k]==time_B[k]:
            num+=1
    for i in range(total_A+1, total_B+1):
        if time_B[i]==time_A[total_A]:
            num+=1
else:
    for k in range(2,total_B+1):
        if time_A[k-1]!=time_B[k-1] and time_A[k]==time_B[k]:
            num+=1
    for i in range(total_B+1, total_A+1):
        if time_A[i]==time_B[total_B]:
            num+=1
print(num)
