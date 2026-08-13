n, m, r, c = map(int, input().split())

# Please write your code here.

r-=1
c-=1

t=0


def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def bomb(x,y,t):
    arr=[]
    if in_range(x-2**(t-1),y):
        arr.append((x-2**(t-1),y))
    if in_range(x+2**(t-1),y):
        arr.append((x+2**(t-1),y))
    if in_range(x,y+2**(t-1)):
        arr.append((x,y+2**(t-1)))
    if in_range(x,y-2**(t-1)):
        arr.append((x,y-2**(t-1)))
    return arr

store=[]
store.append((r,c))

while t<m:
    new=[]
    for elem in store:
        for _ in bomb(elem[0],elem[1],t+1):
            if _ not in store:
                new.append(_)
    for elem in new:
        store.append(elem)
    t+=1
    if t==m:
        break
print(len(store))
    



    
