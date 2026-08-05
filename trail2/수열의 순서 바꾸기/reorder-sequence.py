N = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.

store=sequence
is_continue=True
num=0


if all(store[i]<store[i+1] for i in range(N-1)):
    print(num)
else:
    while is_continue:  
        arr=[]
        for k in range(2,N+1):
            arr=[]
            for elem in store[1:k]:
                arr.append(elem)
            arr.append(store[0])
            for elem in store[k:N]:
                arr.append(elem)
            if all(arr[l]<arr[l+1] for l in range(k-1,N-1)):
                num+=1
                break

        store=arr.copy()

        if all(arr[j]<arr[j+1] for j in range(N-1)):
            is_continue=False
            break
    print(num)