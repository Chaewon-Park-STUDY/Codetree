arr= ["L", "E" , "B", "R", "O", "S"]

N= input()

if N in arr:
    for i in range(6):
        if arr[i] == N:
            print(i)
else:
    print("None")