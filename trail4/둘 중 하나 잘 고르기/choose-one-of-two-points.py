n = int(input())
red = []
blue = []

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# Please write your code here.

arr=[]

blue_sum=sum(blue)

diff=[0 for _ in range(2*n)]
for _ in range(2*n):
    diff[_]=red[_]-blue[_]

diff.sort(reverse=True)
max_val=0

for elem in diff[:n]:
    blue_sum+=elem
print(blue_sum)