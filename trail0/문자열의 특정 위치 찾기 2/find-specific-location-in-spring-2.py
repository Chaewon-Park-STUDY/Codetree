
cnt=input()

arr=["apple", "banana", "grape", "blueberry", "orange"]

num=0
for elem in arr:
    if elem[2]==cnt or elem[3]==cnt:
        print(elem)
        num+=1
print(num)