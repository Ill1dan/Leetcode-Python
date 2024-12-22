from collections import defaultdict
import heapq

def leftmostBuildingQueries(heights, queries):
    res = [-1] * len(queries)

    groups = defaultdict(list)

    for i, q in enumerate(queries):
        l, r = sorted(q)

        if l == r or heights[r] > heights[l]:
            res[i] = r
        else:
            h = max(heights[l], heights[r])
            groups[r].append((h, i))

    min_heap = []
    for i, h in enumerate(heights):

        for q_h, q_i in groups[i]:
            heapq.heappush(min_heap, (q_h, q_i))

        while min_heap and h > min_heap[0][0]:
            q_h, q_i = heapq.heappop(min_heap)
            res[q_i] = i

    return res


heights = [5,3,8,2,6,1,4,6]
queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
print(leftmostBuildingQueries(heights, queries))