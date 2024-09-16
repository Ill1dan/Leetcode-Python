def findMinDifference(timePoints):
    times = []
    for i in timePoints:
        hour, minute = map(int, i.split(":"))
        total_minute = hour * 60 + minute
        times.append(total_minute)

    times.sort()

    res = min([times[i + 1] - times[i] for i in range(len(times) - 1)])

    return min(res, 1440 - times[-1] + times[0])


timePoints = ["23:59", "00:00"]
print(findMinDifference(timePoints))