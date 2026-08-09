n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
#바람이 왼쪽에서 불어오면 오른쪽으로 shift
# 바람이 오른쪽에서 불어오면 왼쪽으로 shift
def in_range(a):
    if 0<=a<=n-1:
        return True


for i in range(q):
    is_continue=True
    is_continue_Down=True
    start=winds[i][0]-1
    down_start=start
    dir=winds[i][1]
    num_up=0
    num_down=0
    if winds[i][1]=="L":
        new=[]
        new.append(a[start][-1])
        for elem in a[start][0:-1]:
            new.append(elem) 
        for j in range(m):
            a[start][j]=new[j]      
        up= start-1
        down=start+1
        while is_continue:
            if in_range(up)==True:
                if any(a[up][j]==a[start][j] for j in range(m)):
                    num_up+=1
                    arr=[]
                    if num_up%2!=0:
                        dir="R"
                    else:
                        dir="L"
                    if dir=="R":
                        for elem in a[up][1:]:
                            arr.append(elem)
                        arr.append(a[up][0])
                        for k in range(m):
                            a[up][k]=arr[k]
                    else:
                        arr.append(a[up][-1])
                        for elem in a[up][0:-1]:
                            arr.append(elem)
                        for k in range(m):
                            a[up][k]=arr[k]
                    up-=1
                    start-=1
                else:
                    is_continue=False
            else:
                is_continue=False

        while is_continue_Down==True:
            if in_range(down)==True:
                if any(a[down][j]==a[down_start][j] for j in range(m)):
                    num_down+=1
                    arr=[]
                    if num_down%2!=0:
                        dir="R"
                    else:
                        dir="L"
                    if dir=="R":
                        for elem in a[down][1:]:
                            arr.append(elem)
                        arr.append(a[down][0])
                        for k in range(m):
                            a[down][k]=arr[k]
                    else:
                        arr.append(a[down][-1])
                        for elem in a[down][0:-1]:
                            arr.append(elem)
                        for k in range(m):
                            a[down][k]=arr[k]
                    down+=1
                    down_start+=1
                else:
                    is_continue_Down=False
            else:
                is_continue_Down=False

    else:
        new=[]
        for elem in a[start][1:]:
            new.append(elem) 
        new.append(a[start][0])   
        for j in range(m):
            a[start][j]=new[j]      
        up= start-1
        down=start+1
        while is_continue:
            if in_range(up)==True:
                if any(a[up][j]==a[start][j] for j in range(m)):
                    num_up+=1
                    arr=[]
                    if num_up%2!=0:
                        dir="L"
                    else:
                        dir="R"
                    if dir=="R":
                        for elem in a[up][1:]:
                            arr.append(elem)
                        arr.append(a[up][0])
                        for k in range(m):
                            a[up][k]=arr[k]
                    else:
                        arr.append(a[up][-1])
                        for elem in a[up][0:-1]:
                            arr.append(elem)
                        for k in range(m):
                            a[up][k]=arr[k]
                    up-=1
                    start-=1
                else:
                    is_continue=False
            else:
                is_continue=False

        while is_continue_Down==True:
            if in_range(down)==True:
                if any(a[down][j]==a[down_start][j] for j in range(m)):
                    num_down+=1
                    arr=[]
                    if num_down%2!=0:
                        dir="L"
                    else:
                        dir="R"
                    if dir=="R":
                        for elem in a[down][1:]:
                            arr.append(elem)
                        arr.append(a[down][0])
                        for k in range(m):
                            a[down][k]=arr[k]
                    else:
                        arr.append(a[down][-1])
                        for elem in a[down][0:-1]:
                            arr.append(elem)
                        for k in range(m):
                            a[down][k]=arr[k]
                    down+=1
                    down_start+=1
                else:
                    is_continue_Down=False
            else:
                is_continue_Down=False


for elem in a:
    for _ in elem:
        print(_, end=" ")
    print()