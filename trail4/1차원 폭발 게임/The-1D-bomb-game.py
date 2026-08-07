n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

# Please write your code here.

is_continue=True

if n==1 and m==1:
    print(0)
else:
    while is_continue:
        new=[]
        arr=[]
        for i in range(len(numbers)-m+1):
            for k in range(2,len(numbers)+1):
                store=[]
                num=k
                for elem in numbers[i:i+k]:
                    if elem not in store:
                        store.append(elem)
                if len(store)==1 and all(numbers[j]==numbers[j+1] for j in range(i,len(numbers)-1)):
                    for j in range(i,len(numbers)):
                        new.append(j)
                    break
                elif len(store)==1:
                    pass
                else:
                    num=k-1
                    if num>=m:
                        for z in range(i,i+num):
                            new.append(z)
                    break
        if len(new)>0:
            for j in range(len(numbers)):
                if j not in new:
                    arr.append(numbers[j])
            numbers=arr
        else:
            is_continue=False
            if len(numbers)>0:
                print(len(numbers))
                for elem in numbers:
                    print(elem)
            else:
                print(0)
    

