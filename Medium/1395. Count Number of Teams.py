def numTeams(rating):
    n = len(rating)
    teams = 0

    for i in range(n):
        leftless = rightmore = leftmore = rightless = 0

        for j in range(0, i):
            if rating[j] < rating[i]:
                leftless += 1
            else:
                leftmore += 1

        for k in range(i + 1, n):
            if rating[k] > rating[i]:
                rightmore += 1
            else:
                rightless += 1

        teams += (leftless * rightmore) + (leftmore * rightless)

    return teams


rating = [2, 5, 3, 4, 1]
print(numTeams(rating))