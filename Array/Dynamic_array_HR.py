first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

q = int(first_multiple_input[1])

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))


def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answer = []

    for query in queries:
        type = query[0]
        x = query[1]
        y = query[2]
        idx = (x ^ lastAnswer) % n

        if type == 1:
            arr[idx].append(y)
        else:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answer.append(lastAnswer)

    return answer


result = dynamicArray(n, queries)
print(result)
