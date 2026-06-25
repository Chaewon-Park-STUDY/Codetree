Y, M, D = map(int, input().split())

# Please write your code here.

arr=[1,3,5,7,8,10,12]
new=[4,6,9,11]


def spring(M):
    if 3<=M<=5:
        return True
def summer(M):
    if 6<=M<=8:
        return True
def fall(M):
    if 9<=M<=11:
        return True
def winter(M):
    if M==12 or M==1:
        return True

def check(Y):
    if Y%4==0:
        if Y%100==0:
            if Y%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def season(Y,M,D):      
    if M in arr:
            if spring(M):
                return "Spring"
            elif summer(M):
                return "Summer"
            elif fall(M):
                return "Fall"
            elif winter(M):
                return "Winter"

    elif M in new:
        if D!=31:
            if spring(M):
                return "Spring"
            elif summer(M):
                return "Summer"
            elif fall(M):
                return "Fall"
        else:
            return -1
    elif M==2:
        if check(Y):
            if 1<=D<=29:
                return "Winter"
            else:
                return -1
        else:
            if 1<=D<=28:
                return "Winter"
            else:
                return -1




print(season(Y,M,D))