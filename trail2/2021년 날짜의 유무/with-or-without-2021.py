M, D = map(int, input().split())

# Please write your code here.

arr=[1,3,5,7,8,10,12]
new=[4,6,9,11]


def check(M,D):
    if M in arr:
        for i in range(1,32):
            if D==i:
                return "Yes"
        return "No"
    elif M in new:
        for i in range(1,31):
            if D==i:
                return "Yes"
        return "No"
    elif M==2:
        if D=="28":
            return "Yes"
        else:
            return "No"
    else:
        return "No"

print(check(M,D))