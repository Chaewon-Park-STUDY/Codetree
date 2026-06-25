A = input()

# Please write your code here.
arr=[]

def logic(A):
    arr=[]
    for elem in A:
        if elem not in arr:
            arr.append(elem)
    if len(arr)>=2:
        return "Yes"
    else:
        return "No"

print(logic(A))