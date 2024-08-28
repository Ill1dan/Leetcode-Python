def countSubIslands(grid1, grid2):
    ROWS, COLS = len(grid1), len(grid1[0])

    def dfs(r, c, visited):
        if r < 0 or c < 0 or r == ROWS or c == COLS or grid2[r][c] == 0 or (r, c) in visited:
            return True

        visited.add((r, c))
        sub_island = grid1[r][c] == 1

        sub_island &= dfs(r + 1, c, visited)
        sub_island &= dfs(r - 1, c, visited)
        sub_island &= dfs(r, c + 1, visited)
        sub_island &= dfs(r, c - 1, visited)

        return sub_island

    visited = set()
    res = 0

    for r in range(ROWS):
        for c in range(COLS):
            if grid2[r][c] and (r, c) not in visited:
                if dfs(r, c, visited):
                    res += 1

    return res


grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
grid2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
print(countSubIslands(grid1, grid2))