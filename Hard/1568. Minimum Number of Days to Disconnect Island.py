def minDays(grid):
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(r, c, visited):
        if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r, c) in visited:
            return
        visited.add((r, c))

        dfs(r + 1, c, visited)
        dfs(r - 1, c, visited)
        dfs(r, c + 1, visited)
        dfs(r, c - 1, visited)

    # Checks if there is 0 or more islands
    visited = set()
    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] and (r, c) not in visited:
                dfs(r, c, visited)
                count += 1

    if count != 1:
        return 0

    # Checks if disconnecting one can divide the island
    island = list(visited)
    for r, c in island:
        grid[r][c] = 0
        visited = set()
        count = 0
        for r2 in range(ROWS):
            for c2 in range(COLS):
                if grid[r2][c2] and (r2, c2) not in visited:
                    dfs(r2, c2, visited)
                    count += 1
        if count != 1:
            return 1
        grid[r][c] = 1

    # If above both false it has to be 2 disconnected to divide the island
    return 2


grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(minDays(grid))