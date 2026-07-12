n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

def is_possible(max_val):
    available_indices=[]
    for i, elem in enumerate(arr):
        if elem<=max_val:
            available_indices.append(i)

    arr_size= len(available_indices)

    if 0 not in available_indices:
        return False

    for i in range(1,arr_size):
        dist=available_indices[i]-available_indices[i-1]
        if dist>k:
            return False

    return True

maximin = 100
for a in range(max(arr[0],arr[-1]),101):
    if is_possible(a):
        maximin = min(maximin, a)

print(maximin)

