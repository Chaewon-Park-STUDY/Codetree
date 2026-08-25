n = int(input())

# Please write your code here.

def detect(arr):
    i=0
    total=0
    store=[]
    if len(arr)==1:
        store.append(0)
    else:
        while i<len(arr)-1:
            if arr[i]!=arr[i+1]:
                store.append(i)
            if i==len(arr)-2 and arr[i]!=arr[i+1]:
                store.append(i+1)
            i+=1
        if len(arr)-1 not in store:
            store.append(len(arr)-1)
    for k in range(len(store)):
        if k==0:
            temp=arr[0:store[k]+1]
        else:
            temp = arr[store[k-1]+1 : store[k]+1]
        if len(temp)%temp[0]==0:
            total+=1
    if total==len(store):
        return True
            
def passing():
    pass


arr=[]
num=0

def choose(n): 
    if len(arr)==n:
        if detect(arr):
            global num
            num+=1
        
        return num
         
    for i in range(1,5):
        arr.append(i)
        choose(n)
        arr.pop()

choose(n)
print(num)