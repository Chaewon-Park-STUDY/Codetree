n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
class Distance():
    def __init__(self, rank,coor):
        self.r= rank
        self.c= coor
Point=[]

for _ in range(n):
    (r,c)= (points[_][0],points[_][1])
    Point.append(Distance(r,c))

Point.sort(key=lambda x: (abs(x.c[0])+abs(x.c[1]), x.r))

for elem in Point:
    print(elem.r+1)