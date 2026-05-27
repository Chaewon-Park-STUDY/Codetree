
arr= list(map(int, input().split()))

odd_sum=0
even_sum=0

for i in range(0,10):
    if i%2==0:
        odd_sum+=arr[i]
    else:
        even_sum+=arr[i]

if odd_sum>=even_sum:
    print(odd_sum- even_sum)
else:
    print(even_sum-odd_sum)



