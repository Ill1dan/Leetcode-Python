from collections import Counter

def kthDistinct(arr, k):
    frequency = Counter(arr)
    count = 0
    for i in frequency:
        if frequency[i] == 1:
            count += 1
            if count == k:
                return i
    return ""


arr = ["d","b","c","b","c","a"]
k = 2
print(kthDistinct(arr, k))