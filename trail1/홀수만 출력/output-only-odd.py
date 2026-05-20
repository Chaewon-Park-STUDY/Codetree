# store=[]
# result= input()
# store+=result
# A= int(store[0])
# B=int(store[2])


# 두자리 이상 넘어가면 실패
A,B= map(int, input(). split())


for num in range(A,B+1):
    if num %2!=0:
        print(num, end= " ")