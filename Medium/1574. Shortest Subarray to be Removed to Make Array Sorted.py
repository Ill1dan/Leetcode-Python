def findLengthOfShortestSubarray(arr):
    # Remove Prefix
    N = len(arr)
    r = N - 1

    while r > 0 and arr[r - 1] <= arr[r]:
        r -= 1

    res = r

    # Remove Postfix
    l = 0
    while l + 1 < N and arr[l] <= arr[l + 1]:
        l += 1

    res = min(res, N - 1 - l)

    # Remove Middle
    l, r = 0, N - 1
    while l < r:
        # Shrink the Valid Window
        while r < N and l + 1 < r and arr[r - 1] <= arr[r] and arr[l] <= arr[r]:
            r -= 1

        # Expand Invalid Window
        while r < N and arr[l] > arr[r]:
            r += 1

        res = min(res, r - l - 1)
        if arr[l] > arr[l + 1]:
            break
        l += 1

    return res


arr = [1, 2, 3, 10, 9, 1, 2, 3]
print(findLengthOfShortestSubarray(arr))