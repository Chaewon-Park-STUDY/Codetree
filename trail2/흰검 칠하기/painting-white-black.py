n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

# x가 1일 때는 이동하지 않음에 유의!

arr=[0 for _ in range(10**5)]
col=[0 for _ in range(10**5)]
change_b=[0 for _ in range(10**5)]
change_w=[0 for _ in range(10**5)]

starting_point=0
store=[]

for i in range(n):
    if dir[i]=="R":
        starting_point+=x[i]
    else:
        starting_point-=x[i]
    store.append(starting_point)

new=-min(store) # 새로운 시작점

for i in range(n):
    if dir[i]=="R":
        for j in range(new,new+x[i]):
            if not(change_b[j]>=2 and change_w[j]>=2):
                arr[j]+=1
                col[j]="B"
                change_b[j]+=1
                
        new+=x[i]-1
    else:
        for j in range(new,new-x[i],-1):
            if not(change_w[j]>=2 and change_b[j]>=2):
                arr[j]+=1
                col[j]="W"
                change_w[j]+=1
                
        new-=x[i]-1
white=0
gray=0
black=0


for i in range(10**5):
    if arr[i]>=2:
        if change_b[i]>=2 and change_w[i]>=2:
            gray+=1
        else:
            if col[i]=="B":
                black+=1
            else:
                white+=1
    elif arr[i]==1:
        if col[i]=="B":
            black+=1
        else:
            white+=1
print(white, black, gray, end=" ")