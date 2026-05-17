arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))
# [1,2,3,4,5]


def reverseArray(a):
    # option 1:
    # return a[::-1]

    # option 2: two pointer method
    left = 0
    right = len(a) - 1
    while left < right:
        # swap
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    return a


res = reverseArray(arr)
print(*res)
