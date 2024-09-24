def longestCommonPrefix(arr1, arr2):
    prefix_hashmap = {}

    for n in arr1:
        while n and n not in prefix_hashmap:
            prefix_hashmap[n] = len(str(n))
            n //= 10

    res = 0
    for n in arr2:
        while n and n not in prefix_hashmap:
            n //= 10

        if n:
            res = max(res, prefix_hashmap[n])

    return res



arr1 = [1, 10, 100]
arr2 = [1000]
print(longestCommonPrefix(arr1, arr2))