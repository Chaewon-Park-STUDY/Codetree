m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

first=[1,3,5,7,8,10,12]
second= [4,6,9,11]
days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"] #요일 집합
start=days[0]
start_index=0
num_count=0

if A=="Mon":
    num_count+=1

while True:
    if m1==m2 and d1==d2:
        break
    d1+=1
    start_index=(start_index+1)%7
    start=days[start_index]
    if start==A:
        num_count+=1

    if m1 in first and d1>31:
        if m1!=12:
            d1=1
            m1+=1
        else:
            m1=1
            d1=1
    elif m1 in second and d1>30:
        d1=1
        m1+=1
    elif m1==2 and d1==30:
        d1=1
        m1+=1

print(num_count)