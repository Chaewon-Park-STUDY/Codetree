h,w= map(int,input().split())
import math

b= 10000*w/h**2


print(math.floor(b))
if b>=25:
    print("Obesity")