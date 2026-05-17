first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

d = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))


# solution 1 using slicing
# def rotateLeft(d, arr):
#     return arr[d:] + arr[:d]


# solution 2 using while loop
def rotateLeft(d, arr):
    rotate = 0
    while d != 0:
        rotate = arr.pop(0)
        arr.append(rotate)
        d -= 1
    return arr


result = rotateLeft(d, arr)
print(result)
