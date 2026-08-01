
N= int(input())

arr=[N+_ for _ in range(100-N+1)]

for elem in arr:
    if elem>=90:
        print("A", end=" ")
    elif elem>=80:
        print("B", end=" ")
    elif elem>=70:
        print("C", end=" ")
    elif elem>=60:
        print("D", end=" ")
    else:
        print("F", end=" ")
