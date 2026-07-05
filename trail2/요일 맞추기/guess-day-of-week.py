m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
first=[1,3,5,7,8,10,12]
second= [4,6,9,11]
week= ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"]
days=0

origin_m1=m1
origin_d1=d1
origin_m2=m2
origin_d2=d2

while True:
        if m1==m2 and d1==d2:
            break
        days+=1
        if m1<m2:
            if m1 in first:
                if d1==31:
                    d1=1
                    m1+=1
                else:
                    d1+=1
            elif m1 in second:
                if d1==30:
                    d1=1
                    m1+=1
                else:
                    d1+=1
            else:
                if d1==28:
                    d1=1
                    m1+=1
                else:
                    d1+=1
        elif m1>m2:
            if m1 in first:
                if m1!=1 and m1!=3 and m1!=8:
                    if d1==1:
                        d1=30
                        m1-=1
                    else:
                        d1-=1
                elif m1==1:
                    if d1==1:
                        d1=31
                        m1-=1
                    else:
                        d1-=1
                elif m1==8:
                    if d1==1:
                        d1=31
                        m1-=1
                    else:
                        d1-=1
                else:
                    if d1==1:
                        d1=28
                        m1-=1
                    else:
                        d1-=1
            elif m1 in second:
                if d1==1:
                    d1=31
                    m1-=1
                else:
                    d1-=1
            else:
                if d1==1:
                    d1=31
                    m1-=1
                else:
                    d1-=1
        else:
            if d1<d2:
                    d1+=1
            else:
                d1-=1

if origin_m1<origin_m2:
    print(week[(days)%7])
elif origin_m1==origin_m2:
    if origin_d1>origin_d2:
        print(week[-(days%7)])
    else:
        print(week[days%7])
else:
    print(week[-(days%7)])

