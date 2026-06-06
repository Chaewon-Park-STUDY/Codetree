a,b,c= map(int, input().split())


if all(i%c!=0 for i in range(a,b+1)):
    print("YES")
else:
    print("NO")