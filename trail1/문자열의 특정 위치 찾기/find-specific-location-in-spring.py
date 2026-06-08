arr= input().split()

for i in range(len(arr[0])):
    if arr[0][i]==arr[1]:
        print(i)
        break

if all(arr[0][i]!=arr[1] for i in range(len(arr[0]))):
    print("No")