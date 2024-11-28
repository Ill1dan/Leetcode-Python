from heapq import heappop, heappush

def minimumObstacles(grid):
    ROWS, COLS = len(grid), len(grid[0])

    min_heap = [(0, 0, 0)]
    visited = set((0, 0))

    while min_heap:
        obstacles, r, c = heappop(min_heap)

        if (r, c) == (ROWS - 1, COLS - 1):
            return obstacles

        neighbours = [[r + 1, c],[r - 1, c], [r, c + 1], [r, c - 1]]
        for nr, nc in neighbours:
            if (nr, nc) in visited or nr < 0 or nc < 0 or nc == COLS or nr == ROWS:
                continue
            heappush(min_heap, (obstacles + grid[nr][nc], nr, nc))
            visited.add((nr, nc))


grid = [[0,1,1],[1,1,0],[1,1,0]]
print(minimumObstacles(grid))