dirs = input()

# Please write your code here.
arr=[]
for elem in dirs:
    arr.append(elem)

new=[]
total=0
num=0
for elem in arr:
    total+=1
    if elem=="L":
        if num!=0:
            new.append(num)
            num=0
        new.append(elem)
    elif elem=="R":
        if num!=0:
            new.append(num)
            num=0
        new.append(elem)
    else:
        num+=1
        if total==len(arr):
            new.append(num)


x,y= 0,0
dx, dy = [1,0,-1,0], [0,-1,0,1]
dir= 3


if all(elem!="F" for elem in arr):
    print(0,0)
elif all(elem=="F" for elem in arr):
    for _ in new:
        print(0,_)
else:
    for i in range(len(new)):
        if new[i]=="L":
            dir= (dir-1+4)%4
        elif new[i]=="R":
            dir= (dir+1)%4
        else:
            x,y= x+ dx[dir]*new[i], y+dy[dir]*new[i]

    print(x,y)