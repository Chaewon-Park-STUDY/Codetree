N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
#온도는 0부터 1000도까지 따짐x -무한대부터 무한대까지!
A= [p[0] for p in ranges]
B= [p[1] for  p in ranges]


def check(temp):
    sum_val=0
    for i in range(N):
        if temp<A[i]:
            sum_val+=C
        elif A[i]<=temp<=B[i]:
            sum_val+=G
        else:
            sum_val+=H
    return sum_val

max_val=0

for temperature in range(1001):
    max_val= max(max_val, check(temperature))

high= H*N
low= C*N

final_max= max(high, low, max_val)
print(final_max)