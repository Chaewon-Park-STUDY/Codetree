x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# Please write your code here.

wid= max(x1,x2,a1,a2)-min(x1,x2,a1,a2)
len= max(y1,y2,b1,b2)-min(y1,y2,b1,b2)

print(max(wid,len)**2)