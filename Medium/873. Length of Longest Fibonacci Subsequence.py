def lenLongestFibSubseq(arr):
    arr_set = set(arr)
    res = 0

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            prev, cur = arr[i], arr[j]
            nxt = prev + cur
            length = 2

            while nxt in arr_set:
                length += 1
                prev, cur = cur, nxt
                nxt = prev + cur
                res = max(res, length)

    return res

arr = [1,2,3,4,5,6,7,8]
print(lenLongestFibSubseq(arr))