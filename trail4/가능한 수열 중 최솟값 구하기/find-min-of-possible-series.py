n = int(input())

# Please write your code here.

arr=[]
num=0

def check(arr):
    letter=''
    for elem in arr:
        letter+=str(elem)
    global num
    num+=1
    print(letter)




def dfs():
    if num==1:
        return 
    if len(arr)==n:
        return check(arr)

    for i in range(4,7):
        if len(arr)==0:
            arr.append(i)
            dfs()
            arr.pop()
        else:
            arr.append(i)
            is_continue=False
            for j in range(1,n):
                if arr[-j:]==arr[-2*j:-j]:
                    is_continue=False
                    break
                else:
                    is_continue=True
            if is_continue:
                dfs()
            arr.pop()
dfs()
