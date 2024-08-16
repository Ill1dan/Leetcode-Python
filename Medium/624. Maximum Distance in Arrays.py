def maxDistance(arrays):
    maximum, minimum = -float("inf"), float("inf")
    diff = 0
    for i in arrays:
        curr_min, curr_max = i[0], i[-1]
        diff = max(diff, curr_max - minimum, maximum - curr_min)
        maximum = max(maximum, curr_max)
        minimum = min(minimum, curr_min)

    return diff


arrays = [[1, 4], [0, 5]]
print(maxDistance(arrays))