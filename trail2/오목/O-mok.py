board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.

num=0
store=[]
for i in range(15):
    for j in range(i,i+5):
        for l in range(15):
            if all(board[j][k]==1 for k in range(l,l+5)):
                if num<1:
                    print(1)
                    print(j+1,l+3)
                    num+=1
                    break
            elif all(board[j][k]==2 for k in range(l,l+5)):
                if num<1:
                    print(2)
                    print(j+1,l+3)
                    num+=1
                    break
            elif all(board[k][j]==1 for k in range(l,l+5)):
                if num<1:
                    print(1)
                    print(l+3,j+1)
                    num+=1
                    break
            elif all(board[k][j]==2 for k in range(l,l+5)):
                if num<1:
                    print(2)
                    print(l+3,j+1)
                    num+=1
                    break


for i in range(12):
    for j in range(i,i+5):
        for l in range(15):
            if all(board[j+k-l][l+4-j-k+l]==1 for k in range(l,l+5)):
                if num<1:
                    print(1)
                    print(j+3,l+3-j)
                    num+=1
                    break
            elif all(board[j+k-l][l+4-j-k+l]==2 for k in range(l,l+5)):
                if num<1:
                    print(2)
                    print(j+3,l+3-j)
                    num+=1
                    break
            elif all(board[j+k-l][k]==1 for k in range(l,l+5)):
                if num<1:
                    print(1)
                    print(j+3,l+3)
                    num+=1
                    break
            elif all(board[j+k-l][k]==2 for k in range(l,l+5)):
                if num<1:
                    print(2)
                    print(j+3,l+3)
                    num+=1
                    break




if num!=1:
    print(0)  





