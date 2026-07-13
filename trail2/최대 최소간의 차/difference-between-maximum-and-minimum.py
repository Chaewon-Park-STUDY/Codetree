n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_cost = 1000000
for a in range(1, 10001):
    cost = 0
    for elem in arr:
        if a <= elem and elem <= a + k:
            continue
        elif elem < a:
            cost += a - elem
        else:
            cost += elem - (a + k)
    
    min_cost = min(min_cost, cost)

print(min_cost)

