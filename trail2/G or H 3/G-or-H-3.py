n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
placed= [0]*10001

for elem in x:
    for _ in range(len(x)):
        if elem==x[_]:
            placed[elem]= c[_]

new=[]
for i in range(1,10001-k):
    sum_value=0
    for j in range(i,i+k+1):
        if placed[j]=="G":
            sum_value+=1
        elif placed[j]=="H":
            sum_value+=2
        else:
            pass
    new.append(sum_value)
print(max(new))
