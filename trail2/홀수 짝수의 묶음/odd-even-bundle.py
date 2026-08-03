N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.

even=[]
odd=[]
for elem in numbers:
    if elem%2==0:
        even.append(elem)

    else:
        odd.append(elem)


num=0
if len(even)!=len(odd):
        if len(even)<len(odd):
            if len(even)==1 and len(odd)==2:
                num=1
            else:
                store=len(odd)-len(even)
                if (store+1)%3==0:
                    num+=2*len(even)+2*((store+1)//3)-1
                elif (store)%3==0:
                    num+=2*len(even)+((store)//3)*2
                else:
                    num+=2*len(even)+2*((store-1)//3)-1
        else:
            num+=2*len(odd)+1
else:
    num=len(numbers)
print(num)


