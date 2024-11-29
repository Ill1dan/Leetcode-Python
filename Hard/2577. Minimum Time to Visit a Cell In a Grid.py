from heapq import heappop, heappush

def minimumTime(grid):
    if min(grid[0][1], grid[1][0]) > 1:
        return -1

    ROWS, COLS = len(grid), len(grid[0])
    min_heap = [(0, 0, 0)]
    visited = set()

    while min_heap:
        t, r, c = heappop(min_heap)

        if (r, c) == (ROWS - 1, COLS - 1):
            return  t

        neighbours = [[r + 1, c],[r - 1, c], [r, c + 1], [r, c - 1]]
        for nr, nc in neighbours:
            if (nr, nc) in visited or nr < 0 or nc < 0 or nc == COLS or nr == ROWS:
                continue
            wait = 0

            if (grid[nr][nc] - t) % 2 == 0:
                wait = 1

            next_t = max(grid[nr][nc] + wait, t + 1)
            heappush(min_heap, (next_t, nr, nc))
            visited.add((nr, nc))

grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
print(minimumTime(grid))