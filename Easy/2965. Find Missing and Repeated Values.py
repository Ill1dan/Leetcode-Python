from collections import defaultdict

def findMissingAndRepeatedValues(grid):
    N = len(grid)
    count = defaultdict(int)

    for i in range(N):
        for j in range(N):
            count[grid[i][j]] += 1

    double, missing = 0, 0

    for num in range(1, N * N + 1):
        if count[num] == 2:
            double = num
        elif count[num] == 0:
            missing = num

    return [double, missing]


grid = [[1,3],[2,2]]
print(findMissingAndRepeatedValues(grid))