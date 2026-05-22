
N= int(input())

for num in range(1, N+1):
    if num%3==0:
        print(0, end= " ")
    elif (num - (num//10)) %3==0 and num%10!=0:
        print(0, end= " ")
    elif 1<= num%30 <=9 and num>=10:
       print(0, end= " ")
    else:
        print(num, end= " ")