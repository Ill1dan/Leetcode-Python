def survivedRobotsHealths(positions, healths, directions):
    n = len(positions)
    indexes = list(range(n))
    indexes.sort(key=lambda x: positions[x])
    robots = [[positions[x], healths[x], directions[x], x] for x in range(n)]

    stack = []
    for i in indexes:
        sub = [robots[i][0], robots[i][1], robots[i][2], robots[i][3]]

        if len(stack) == 0:
            stack.append(sub)

        elif stack[-1][2] == "R" and sub[2] == "L":
            if stack[-1][1] < sub[1]:
                while stack[-1][1] < sub[1]:
                    stack.pop(-1)
                    sub[1] -= 1
                    if stack:
                        if stack[-1][1] > sub[1] and stack[-1][2] == "R":
                            stack[-1][1] -= 1
                            sub[1] = 0
                        elif stack[-1][1] == sub[1] and stack[-1][2] == "R":
                            stack.pop(-1)
                            sub[1] = 0
                    if len(stack) == 0 or stack[-1][2] == "L":
                        break

                if sub[1] > 0:
                    stack.append(sub)
            elif stack[-1][1] == sub[1]:
                stack.pop(-1)
            else:
                stack[-1][1] -= 1
                if stack[-1][1] == 0:
                    stack.pop(-1)
        else:
            stack.append(sub)


    stack.sort(key=lambda x: x[3])

    return [x[1] for x in stack]

positions = [3,2,30,24,38,7]
healths = [47,12,49,11,47,38]
directions = "RRLRRR"

print(survivedRobotsHealths(positions, healths, directions))