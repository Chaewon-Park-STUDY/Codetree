A = input()

# Please write your code here.
store=[]
min_val=10000
if len(A)==1:
    print(2)
else:
    for i in range(1,len(A)):
        new=''
        new+=A[-i:]
        new+=A[0:-i]
        arr=''
        num=1
        for j in range(len(new)-1):
            if new[j]==new[j+1]:
                num+=1
            else:
                store=[]
                if j==len(new)-2:
                    arr+=new[j]
                    arr+=str(num)
                    arr+=new[j+1]
                    arr+=str(1)
                else:
                    for elem in new[j+1:]:
                        if elem not in store:
                            store.append(elem)
                    if len(store)==1:
                        arr+=new[j]
                        arr+=str(num)
                        arr+=new[j+1]
                        arr+=str(len(new)-(j+1))
                    else:
                        arr+=new[j]
                        arr+=str(num)
                        num=1
        if all(new[j]==new[j+1] for j in range(len(new)-1)):
            arr+=new[j]
            arr+=str(len(new))

        min_val=min(min_val,len(arr))
      
    print(min_val)

