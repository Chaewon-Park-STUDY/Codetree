S, Q= list(map(str, input().split()))

arr=[]
for i in range(int(Q)):
    arr.append(list(input().split()))
S=list(S)




for i in range(int(Q)):
    S=list(S)
    num=''
    if arr[i][0]=="1":
        m= S[int(arr[i][1])-1]
        n= S[int(arr[i][2])-1]
        S[int(arr[i][1])-1]= n
        S[int(arr[i][2])-1]= m
        for elem in S:
            print(elem,end="")
        print()
    else:
        for elem in S:
            if elem== arr[i][1]:
                elem= arr[i][2]
            num+=elem
        S=num
        print(num)