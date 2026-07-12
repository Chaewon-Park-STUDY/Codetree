nums = list(map(int, input().split()))

# Please write your code here.

def is_equal_array(arr1, arr2):
    arr1.sort()
    arr2.sort()

    if len(arr1) != len(arr2):
        return False

    for x, y in zip(arr1, arr2):
        if x != y:
            return False

    return True

for a in range(1, 40):
    for b in range(a, 40):
        for c in range(b, 40):
            for d in range(c,40):
                if is_equal_array([a,b,c,d,a+b,b+c,c+d,d+a,a+c,b+d,a+b+c,a+b+d,a+c+d,b+c+d,a+b+c+d], nums):
                    print(a, b, c,d)


