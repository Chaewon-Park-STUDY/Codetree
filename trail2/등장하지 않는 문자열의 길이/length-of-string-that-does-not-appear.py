N = int(input())
str = input()

# Please write your code here.
max_val=0
new=[]
for i in range(N):
    for j in range(100):
        for l in range(1,N-1-i):
            if str[i:i+j]==str[i+l:i+l+j]:
                new.append(j)
print(max(new)+1)


