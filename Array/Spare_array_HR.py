stringList_count = int(input().strip())

stringList = []

for _ in range(stringList_count):
    stringList_item = input()
    stringList.append(stringList_item)

queries_count = int(input().strip())

queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

# option 1 (brute force)


# def matchingStrings(stringList, queries):
#     q = []
#     for i in range(len(queries)):
#         count = 0
#         for j in range(len(stringList)):
#             if queries[i] == stringList[j]:
#                 count += 1
#         q.append(count)
#     return q


# option 2 (efficient) using count method)


def matchingStrings(stringList, queries):
    frequencies = {}
    result = []
    for string in stringList:
        frequencies[string] = frequencies.get(string, 0) + 1
    for query in queries:
        result.append(frequencies.get(query, 0))
    return result


res = matchingStrings(stringList, queries)
print(res)
