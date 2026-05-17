arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))


# solution 1
# def hourglassSum(arr):
#     max_Sum = -float("inf")
#     for i in range(4):
#         for j in range(4):
#             top = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
#             middle = arr[i + 1][j + 1]
#             bottom = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
#             current_sum = top + middle + bottom

#             if current_sum > max_Sum:
#                 max_Sum = current_sum

#     return max_Sum

# solution 2
def hourglassSum(arr):
    max_Sum = -float("inf")
    for i in range(4):
        for j in range(4):
            current_sum = (
                arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                arr[i + 1][j + 1] +
                arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            )
            if current_sum > max_Sum:
                max_Sum = current_sum

    return max_Sum


result = hourglassSum(arr)
print(result)
