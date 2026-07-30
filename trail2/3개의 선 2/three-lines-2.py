n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

new_x=[]
new_y=[]


for elem in x:
    if elem not in new_x:
        new_x.append(elem)
for elem in y:
    if elem not in new_y:
        new_y.append(elem)
a=len(new_x)
b=len(new_y)

def determine(x,y):
    num=0

    if x==0 and y==3:
        for i in range(b-2):
            for j in range(i+1,b-1):
                for k in range(j+1,b):
                    arr=[new_y[i],new_y[j],new_y[k]]
                    store=[]
                    for elem in points:
                        if elem[1] in arr:
                            if elem not in store:
                                store.append(elem)
                    if len(store)==n:
                        num+=1
    
    elif x==3 and y==0:
        for i in range(a-2):
            for j in range(i+1,a-1):
                for k in range(j+1,a):
                    arr=[new_x[i],new_x[j],new_x[k]]
                    store=[]
                    for elem in points:
                        if elem[0] in arr:
                            if elem not in store:
                                store.append(elem)
                    if len(store)==n:
                        num+=1

    elif x==1 and y==2:
        for i in range(a):
            for j in range(b-1):
                for k in range(j+1,b):
                    arr=[new_x[i],new_y[j],new_y[k]]
                    store=[]
                    for elem in points:
                        if elem[0]==new_x[i]:
                            if elem not in store:
                                store.append(elem)
                        if elem[1]==new_y[j] or elem[1]==new_y[k]:
                            if elem not in store:
                                store.append(elem)
                    if len(store)==n:
                        num+=1


    elif x==2 and y==1:
        for i in range(b):
            for j in range(a-1):
                for k in range(j+1,a):
                    arr=[new_y[i],new_x[j],new_x[k]]
                    store=[]
                    for elem in points:
                        if elem[1]==new_y[i]:
                            if elem not in store:
                                store.append(elem)
                        if elem[0]==new_x[j] or elem[0]==new_x[k]:
                            if elem not in store:
                                store.append(elem)
                    if len(store)==n:
                        num+=1
    return num


if any(determine(x,3-x)>=1 for x in range(0,4)):
    print(1)
else:
    print(0)