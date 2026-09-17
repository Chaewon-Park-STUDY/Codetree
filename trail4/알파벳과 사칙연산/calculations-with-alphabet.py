expression = input()

# Please write your code here.

def calculate(m,l,p,visited):
    if l=="+":
        if type(m)!=int:
            return visited.get(m)+visited.get(p)
        else:
            return m+visited.get(p)
    elif l=="-":
        if type(m)!=int:
            return visited.get(m)-visited.get(p)
        else:
            return m-visited.get(p)
    else:
        if type(m)!=int:
            return visited.get(m)*visited.get(p)
        else:
            return m*visited.get(p)


num_count=0 

alphabet=[]
store=[]


max_val=-10**10
for elem in expression:
    if elem.isalpha()==True:
        if elem not in alphabet:
            alphabet.append(elem)
    else:
        num_count+=1
    store.append(elem)

n= len(alphabet)
alphabet.sort()
arr=[]


def check(arr):


    visited={}
    for i in range(len(alphabet)):
        visited[alphabet[i]]=arr[i]
    
    global max_val
    b=0
    candid= store.copy()
    while b<num_count:
        result=calculate(candid[0],candid[1],candid[2],visited)
        for j in range(3):
            candid.pop(0)
        candid.insert(0,result)
        b+=1
    if len(expression)==1:
        max_val=4
    else:
        max_val=max(max_val,candid[0])
            
        
def dfs():
    if len(arr)==n:
        return check(arr)
    for i in range(1,5):
        arr.append(i)
        dfs()
        arr.pop()

dfs()
print(max_val)







