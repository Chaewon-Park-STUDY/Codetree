
arr= list(map(int, input().split()))


for num in arr:
    if num==0:
        break
    else:
        if num%2!=0:
            num+=3
            print(num, end= " ")
        else:
            print(num//2, end= " ")