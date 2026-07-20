n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.

store=[]
for i in range(n):
    store.append((pos[i],alpha[i]))
store.sort()

max_len=0
for i in range(n-1):
    num_G=0
    num_H=0
    if store[i][1]=="G":
        num_G+=1
        for j in range(i+1,n):
            if store[j][1]=="G":
                num_G+=1
            else:
                num_H+=1
            if num_G==num_H or num_G==0 or num_H==0:
                length=store[j][0]-store[i][0]
                max_len= max(max_len, length)
    else:
        num_H+=1
        for j in range(i+1,n):
            if store[j][1]=="G":
                num_G+=1
            else:
                num_H+=1
            if num_G==num_H or num_G==0 or num_H==0:
                length=store[j][0]-store[i][0]
                max_len= max(max_len, length)
print(max_len)