commands = input()

# Please write your code here.
arr=[]
for elem in commands:
    arr.append(elem)
dxs,dys= [1,0,-1,0],[0,-1,0,1]
x,y=0,0
dir_num= 3
time=0

for i in arr:
    time+=1
    if i=="F":
        x,y= x+ dxs[dir_num], y+dys[dir_num]
        if x==0 and y==0:
            print(time)
            exit()
    elif i=="L":
        dir_num= (dir_num-1+4)%4
    else:
        dir_num= (dir_num+1)%4
print(-1)