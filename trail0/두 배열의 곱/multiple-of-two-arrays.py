
arr1=[list(map(int,input().split())) for _ in range(3)]
space=input()
arr2=[list(map(int,input().split())) for _ in range(3)]


new=[
    [1 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        new[i][j]=arr1[i][j]*arr2[i][j]


for elem in new:
    for _ in elem:
        print(_, end=" ")
    print()