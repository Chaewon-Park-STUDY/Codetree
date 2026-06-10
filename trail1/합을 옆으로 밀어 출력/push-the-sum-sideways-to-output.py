N= int(input())
arr=[]
result=0

for i in range(N):
    arr.append(int(input()))

for elem in arr:
    result+=elem

# result= str(result)
# new= result[1::] + result[0]
# print(new)

result= list(str(result))
a= result[0]
result.pop(0)
s=''.join(result)+str(a)
print(s)