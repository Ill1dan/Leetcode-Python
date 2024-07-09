def averageWaitingTime(customers):

    time = 0
    avg_time = 0

    for x in customers:
        if time < x[0]:
            time = x[0]
        time += x[1]
        avg_time += time - x[0]

    return avg_time / len(customers)

arr = [[5,2],[5,4],[10,3],[20,1]]
print(averageWaitingTime(arr))