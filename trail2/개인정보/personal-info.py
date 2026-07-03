n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.

class Name():
    def __init__(self,n,h,w):
        self.n= n
        self.h=h
        self.w=w
students=[]

for _ in range(5):
    (n,h,w)= (name[_], height[_], weight[_])
    students.append(Name(n,h,w))

students.sort(key=lambda x: x.n)
print("name")
for elem in students:
    print(elem.n, elem.h, elem.w)
print()
students.sort(key=lambda x: -x.h)

print("height")
for elem in students:
    print(elem.n, elem.h, elem.w)

