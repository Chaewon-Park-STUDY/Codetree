n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

answer_list=[]


for i in range(0,n-1):
    for k in range(n-i,1,-1):
        sum_value=arr[i]
        for j in range(i+1, i+k):
            sum_value+=arr[j]
        avg_value= sum_value/(k)
        for _ in range(i,i+k):
            if arr[_]==avg_value:
                answer_list.append(avg_value)
                break

print(len(answer_list)+n)
