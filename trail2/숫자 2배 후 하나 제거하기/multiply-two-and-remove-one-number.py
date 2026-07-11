n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
min_val=10000
for i in range(n):
    arr[i]*=2

    for j in range(n):
        sum_diff=0
        new=[]
        for l in range(n):
            if l!=j:
                new.append(arr[l])
        for k in range(n-2): 
            sum_diff+=abs(new[k]-new[k+1])
        min_val=min(min_val, sum_diff)
    arr[i]//=2 
        
print(min_val)
        
        
