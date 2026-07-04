a,b,c= map(int, input().split())

num=a+b+c
avg= num//3
answer= num-avg

print(num,avg,answer,sep="\n")