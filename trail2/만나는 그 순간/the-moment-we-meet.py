n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.

start=0
A=[]
B=[]
for i in range(n):
    if d[i]=="R":
        start+=t[i]
    else:
        start-=t[i]
    A.append(start)

start=0

for j in range(m):
    if d2[j]=="R":
        start+=t2[j]
    else:
        start-=t2[j]
    B.append(start)
start=0
a=min(A)
b=min(B)

if min(a,b)<0:
    start+=-min(a,b)

arr_A=[0 for _ in range(10**6)]
time_A=[0 for _ in range(10**6)]
arr_B=[0 for _ in range(10**6)]
time_B=[0 for _ in range(10**6)]


num_A=1

cnt=start
time_A[0]=start

for i in range(n):
    if d[i]=="R":
        for j in range(1,t[i]+1):
            time_A[num_A]=start+j
            num_A+=1
        start+=t[i]
    else:
        for j in range(1,t[i]+1):
            time_A[num_A]=start-j
            num_A+=1
        start-=t[i]

num_B=1
time_B[0]=cnt


for i in range(m):
    if d2[i]=="R":
        for j in range(1,t2[i]+1):
            time_B[num_B]=cnt+j
            num_B+=1
        cnt+=t2[i]
    else:
        for j in range(1,t2[i]+1):
            time_B[num_B]=cnt-j
            num_B+=1
        cnt-=t2[i]

total_A=sum(t)
total_B=sum(t2)
success=0
for i in range(1,max(total_A,total_B)+1):
    if time_A[i]==time_B[i]:
        success+=1
        print(i)
        break
if success==0:
    print(-1)
