a,b,c= map(int, input().split())


arr=[]
for i in range(a, b+1):
    if i%c==0:
        arr.append(i)
    else:
        pass

if len(arr)>0:
    print("YES")
else:
    print("NO")