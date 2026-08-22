n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dxs,dys=[-1,0,1,0],[0,-1,0,1]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m


possible=[[0 for _ in range(m)]for _ in range(n)]
num=[[1000000 for _ in range(m)]for _ in range(n)]



def move(x,y,number):
    arr=[]
    for i in range(4):
        nx,ny=x+dxs[i],y+dys[i]
        if in_range(nx,ny) and number+1<num[nx][ny] and a[nx][ny]!=0:
            arr.append((nx,ny))
    if len(arr)>0:
        return arr
    return False


if a[0][0]!=0:
    is_continue=True
    stack=[]
    final=[]
    number=0
    x,y=0,0
    possible[x][y]="X"
    num[x][y]=number
    while is_continue:
        if x==n-1 and y==m-1:
            final.append(num[x][y])
            is_continue=False
            break
            # if len(stack)==0:
            #     is_continue=False
            #     break
            # else:
            #     x,y,number=stack.pop()
            #     continue
        if move(x,y,number)==False:
            if stack:
                x,y,number=stack.pop(0)
            else:
                is_continue=False
                break
        
        else:
            for nx,ny in move(x,y,number):
                next_num=number+1
                num[nx][ny]=next_num
                stack.append((nx,ny,next_num))
            x,y,number=stack.pop(0)
            

    if len(final)>0:
        print(min(final))
    else:
        print(-1)



