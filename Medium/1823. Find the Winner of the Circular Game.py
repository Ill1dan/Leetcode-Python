def findTheWinner(n, k):
    friends = [x for x in range(1, n + 1)]
    pointer = 0

    while len(friends) > 1:
        to_pop = (pointer + k - 1) % len(friends)
        friends.pop(to_pop)
        pointer = to_pop

    return friends[0]







findTheWinner(6, 5)