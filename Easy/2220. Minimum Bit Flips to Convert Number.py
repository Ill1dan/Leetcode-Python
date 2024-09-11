def minBitFlips(start, goal):
    res = start ^ goal
    return bin(res).count("1")


start = 10
goal = 7
print(minBitFlips(start, goal))