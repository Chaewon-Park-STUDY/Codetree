n, m = map(int, input().split())

# Please write your code here.

# solution1)
# for i in range(n):
#     for j in range(m):
#         print(1,end="")
#     print()

#solution2) 함수 이용한 풀이
def logic():
    print("1"*m)

for i in range(n):
    logic()