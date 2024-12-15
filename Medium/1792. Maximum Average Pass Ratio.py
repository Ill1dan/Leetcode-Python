import heapq

def maxAverageRatio(classes, extraStudents):
    classes_with_prob = []

    for i, j in classes:
        heapq.heappush(classes_with_prob, [i / j - (i + 1) / (j + 1), i, j])


    for _ in range(extraStudents):
        least_prob = heapq.heappop(classes_with_prob)
        updated_prob = [(least_prob[1] + 1) / (least_prob[2] + 1) - (least_prob[1] + 2) / (least_prob[2] + 2), least_prob[1] + 1, least_prob[2] + 1]
        heapq.heappush(classes_with_prob, updated_prob)

    return sum([i / j for _, i, j in classes_with_prob]) / len(classes_with_prob)


classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
print(maxAverageRatio(classes, extraStudents))