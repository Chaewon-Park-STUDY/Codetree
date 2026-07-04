m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
first=[1,3,5,7,8,10,12]
second=[4,6,9,11]


days=1
while True:
    if m1==m2 and d1==d2:
        break

    days+=1
    if m1 in first: 
        if d1!=31:
            d1+=1
        else:
            d1=1
            m1+=1
    elif m1 in second:
        if d1!=30:
            d1+=1
        else:
            d1=1
            m1+=1
    elif m1==2:
        if d1!=28:
            d1+=1
        else:
            m1+=1
            d1=1

print(days)
    
