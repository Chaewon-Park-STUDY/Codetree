a, b = map(int, input().split())

# Please write your code here.

store=[]
def is_True(n):
    if n<10:
        store.append(n)
        return store
    
    store.append(n%10)
    return is_True(n//10)

num=0
for i in range(a,b+1):
    if i%3==0:
        num+=1
    else:
        store=[]
        new=is_True(i)
        if any(elem!=0 and elem%3==0 for elem in new):
            num+=1
print(num)

