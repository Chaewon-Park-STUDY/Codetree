N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
store=[]

for i in range(1,N+1):
    if abs(i-a1)<=2 or abs(i-a1)==N-1 or abs(i-a1)==N-2:
        for j in range(1,N+1):
            if abs(j-b1)<=2 or abs(j-b1)==N-1 or abs(j-b1)==N-2:
                for k in range(1,N+1):
                    if abs(k-c1)<=2 or abs(k-c1)==N-1 or abs(k-c1)==N-2:
                            store.append((i,j,k))

for i in range(1,N+1):
    if abs(i-a2)<=2 or abs(i-a2)==N-1 or abs(i-a2)==N-2:
        for j in range(1,N+1):
            if abs(j-b2)<=2 or abs(j-b2)==N-1 or abs(j-b2)==N-2:
                for k in range(1,N+1):
                    if abs(k-c2)<=2 or abs(k-c2)==N-1 or abs(k-c2)==N-2:
                        if (i,j,k) not in store:
                            store.append((i,j,k))
print(len(store))