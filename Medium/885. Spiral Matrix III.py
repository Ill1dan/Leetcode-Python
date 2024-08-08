def spiralMatrixIII(rows, cols, rStart, cStart):
    res = [[rStart, cStart]]
    current_coordinate = [rStart, cStart]
    increment = 0
    while len(res) < rows * cols:
        increment += 1

        for i in range(increment):
            current_coordinate = [current_coordinate[0], current_coordinate[1] + 1]
            if current_coordinate[1] < cols and current_coordinate[0] < rows and current_coordinate[1] >= 0 and current_coordinate[0] >= 0:
                res.append(current_coordinate)

        for j in range(increment):
            current_coordinate = [current_coordinate[0] + 1, current_coordinate[1]]
            if current_coordinate[1] < cols and current_coordinate[0] < rows and current_coordinate[1] >= 0 and current_coordinate[0] >= 0:
                res.append(current_coordinate)

        increment += 1

        for x in range(increment):
            current_coordinate = [current_coordinate[0], current_coordinate[1] - 1]
            if current_coordinate[1] < cols and current_coordinate[0] < rows and current_coordinate[1] >= 0 and current_coordinate[0] >= 0:
                res.append(current_coordinate)

        for y in range(increment):
            current_coordinate = [current_coordinate[0] - 1, current_coordinate[1]]
            if current_coordinate[1] < cols and current_coordinate[0] < rows and current_coordinate[1] >= 0 and current_coordinate[0] >= 0:
                res.append(current_coordinate)

    return res


rows = 5
cols = 6
rStart = 1
cStart = 4
print(spiralMatrixIII(rows, cols, rStart, cStart))