board = [list(input()) for _ in range(10)]

# Please write your code here.
import random

for i in range(10):
    for j in range(10):
        if board[i][j]=="B":
            B= (i,j)
        elif board[i][j]=="R":
            R= (i,j)
        elif board[i][j]=="L":
            L=(i,j)


if L[0]==R[0]==B[0]:
    if B[1]<R[1]<L[1] or L[1]<R[1]<B[1]:
        print(abs(B[1]-L[1])+1)
    else:
        print(abs(B[1]-L[1])-1)
elif L[1]==R[1]==B[1]:
    if (B[0]<R[0]<L[0] or L[0]<R[0]<B[0]):
        print(abs(B[0]-L[0])+1) 
    else:
        print(abs(L[0]-B[0])-1)
else:
    print(abs(L[0]-B[0])+abs(L[1]-B[1])-1)




