def robotSim(commands, obstacles):
    obstacle_set = set(map(tuple, obstacles))

    x, y = 0, 0
    directions = ["West", "North", "East", "South"]
    start = 1
    max_euclidean_distance = 0

    for i in commands:
        if i == -1:
            start = (start + 1) % 4
        elif i == -2:
            start = (start - 1) % 4
        else:
            curr_direction = directions[start]

            for j in range(1, i + 1):
                new_x, new_y = x, y

                if curr_direction == "North":
                    new_y += j
                elif curr_direction == "South":
                    new_y -= j
                elif curr_direction == "East":
                    new_x += j
                else:
                    new_x -= j

                if (new_x, new_y) in obstacle_set:
                    if curr_direction == "North":
                        new_y -= 1
                    elif curr_direction == "South":
                        new_y += 1
                    elif curr_direction == "East":
                        new_x -= 1
                    else:
                        new_x += 1
                    break

            x, y = new_x, new_y
            max_euclidean_distance = max(max_euclidean_distance, x ** 2 + y ** 2)

    return max_euclidean_distance


commands = [6, -1, -1, 6]
obstacles = []
print(robotSim(commands, obstacles))