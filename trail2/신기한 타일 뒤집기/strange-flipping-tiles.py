n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
starting_point=0
store=[]
for i in range(n):
    if dir[i]=="R":
        starting_point+=x[i]
    else:
        starting_point-=x[i]
    store.append(starting_point)

new= -min(store) #새로운 시작점

col=[0 for _ in range(10000)]

for i in range(n):
    if dir[i]=="R":
        for j in range(new, new+x[i]):
            col[j]="B"
        new+=x[i]-1
    else:
        for j in range(new,new-x[i],-1):
            col[j]="W"
        new-=x[i]-1
black=0
white=0

for elem in col:
    if elem=="B":
        black+=1
    elif elem=="W":
        white+=1
print(white, black, end=" ")