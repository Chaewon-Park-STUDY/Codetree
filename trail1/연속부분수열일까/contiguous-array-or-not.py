N1, N2= map(int, input().split())

A= list(map(int, input().split()))

B= list(map(int, input().split()))

no_count=0
yes_count=0
if len(B)==1:
    for elem in B:
        if elem in A:
            print("Yes")
        else:
            print("No")
elif len(A)==1 and len(B)==1:
    for elem in A:
        if elem in B:
            print("Yes")
        else:
            print("No")
else:
    for i in range(len(A)-1):
        #if A[len(A)-1] != B[0]:
            if all(A[i+_]==B[_] for _ in range(len(B))):
                print("Yes")
                yes_count+=1
                break
            else:
                no_count+=1
        # else:
        #     print("No")
        #     break
if yes_count<1 and no_count>1:
    if len(B)!=1 and not(len(A)==1 and len(B)==1) or len(B)>len(A):
        print("No")