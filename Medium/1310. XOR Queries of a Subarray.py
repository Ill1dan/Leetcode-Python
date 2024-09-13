def xorQueries(arr, queries):
    prefix = [0]
    for n in arr:
        prefix.append(prefix[-1] ^ n)

    res = []
    for left, right in queries:
        res.append(prefix[right + 1] ^ prefix[left])

    return res

arr = [1, 3, 4, 8]
queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
print(xorQueries(arr, queries))