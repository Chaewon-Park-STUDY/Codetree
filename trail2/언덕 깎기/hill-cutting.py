N = int(input())
heights = [int(input()) for _ in range(N)]

# Please write your code here.

heights.sort()


a=min(heights)
b=a+17

min_val=10**8
if max(heights)-min(heights)>17:
    for i in range(1000):
        new=0
        a+=1
        b+=1
        for k in range(N):
            if heights[k]<=a:
                new+=(a-heights[k])**2
            if heights[k]>=b:
                new+=(heights[k]-b)**2


        min_val=min(min_val,new)
    print(min_val)
else:
    print(0)