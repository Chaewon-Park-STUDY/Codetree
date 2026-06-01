arr=[]

for _ in range(2):
    arr_1d= list(map(int, input().split()))
    arr.append(arr_1d)


row_avg1, row_avg2= round(sum(arr[0])/4, 1), round(sum(arr[1])/4, 1)
print(row_avg1, row_avg2, end= " ")
print()

for i in range(4):
    col_avg= round((arr[0][i] + arr[1][i])/2, 1)
    print(col_avg, end= " ")

print()

row_sum=0
for i in range(4):
    row_sum+= arr[0][i]+ arr[1][i]
all_avg= round(row_sum/8,1)
print(all_avg)

