N = int(input())
seat = input()

# Please write your code here.
seat=list(map(int, list(seat)))

def seat_check(a):
    taken=[]
    num=[]
    for i,elem in enumerate(seat):
        if elem==1:
            taken.append(i)

    for i in range(a):
        if seat[i]==0:
            for j in range(i+1,a):
                if seat[j]==0:
                    copy = taken.copy()
                    min_val=100
                    copy.append(i)
                    copy.append(j)
                    copy.sort()
                    for k in range(1,len(copy)):
                        dist=copy[k]-copy[k-1]
                        min_val= min(min_val,dist)
                    num.append(min_val)


    return max(num)
print(seat_check(N))


