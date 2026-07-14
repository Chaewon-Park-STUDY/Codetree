a, b, x, y = map(int, input().split())
# Please write your code here.
dist=0
first=abs(a-b)
second= abs(a-x)+abs(b-y)
third= abs(a-y)+abs(b-x)


store=[]
store.append(first)
store.append(second)
store.append(third)
store.sort()

if store[0]==first:
    dist+=first
elif store[0]==second:
    dist+=second
else:
    dist+=third
print(dist)
