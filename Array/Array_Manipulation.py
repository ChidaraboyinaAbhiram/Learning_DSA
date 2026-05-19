first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))


def arrayManipulation(n, queries):
    arr = [0] * (n+2)
    for a, b, k in queries:
        arr[a] += k
        arr[b+1] -= k
    max_val = 0
    current_val = 0
    for val in arr:
        current_val += val
        if current_val > max_val:
            max_val = current_val
    return max_val


result = arrayManipulation(n, queries)
print(result)