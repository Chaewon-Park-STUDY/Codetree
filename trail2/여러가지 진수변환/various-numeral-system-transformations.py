N, B = map(int, input().split())

# Please write your code here.
arr=[]
while B==4:
    if N<4:
        arr.append(N)
        break
    arr.append(N%4)
    N//=4
if B==4:    
    for elem in arr[::-1]:
        print(elem,end="")

while B==8:
    if N<8:
        arr.append(N)
        break
    arr.append(N%8)
    N//=8
if B==8:    
    for elem in arr[::-1]:
        print(elem,end="")
        
