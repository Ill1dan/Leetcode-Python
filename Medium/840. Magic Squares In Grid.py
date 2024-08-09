def numMagicSquaresInside(grid):
    ROWS, COLS = len(grid), len(grid[0])
    res = 0

    def magic(r, c):
        digits = set()
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if grid[i][j] in digits or not(1 <= grid[i][j] <= 9):
                    return 0
                digits.add(grid[i][j])

        for i in range(r, r + 3):
            if sum(grid[i][c:c+3]) != 15:
                return 0

        for i in range(c, c + 3):
            if sum((grid[r][i], grid[r + 1][i], grid[r + 2][i])) != 15:
                return 0

        if sum((grid[r][c], grid[r + 1][c + 1], grid[r + 2][c + 2])) != 15 or sum((grid[r][c + 2], grid[r + 1][c + 1], grid[r + 2][c])) != 15:
            return 0

        return 1


    for r in range(ROWS - 2):
        for c in range(COLS - 2):
            res += magic(r, c)

    return res


grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
print(numMagicSquaresInside(grid))