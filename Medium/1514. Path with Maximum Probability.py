from heapq import heappop, heappush
from collections import defaultdict


def maxProbability(n, edges, succProb, start_node, end_node):
    graph = defaultdict(list)
    for i, (a, b) in enumerate(edges):
        graph[a].append((b, succProb[i]))
        graph[b].append((a, succProb[i]))

    max_heap = [(-1.0, start_node)]
    max_prob = [0.0] * n
    max_prob[start_node] = 1.0

    while max_heap:
        current_prob, node = heappop(max_heap)
        current_prob = -current_prob

        if node == end_node:
            return current_prob

        for neighbor, edge_prob in graph[node]:
            new_prob = current_prob * edge_prob
            if new_prob > max_prob[neighbor]:
                max_prob[neighbor] = new_prob
                heappush(max_heap, (-new_prob, neighbor))

    return 0.0


n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2

print(maxProbability(n, edges, succProb, start, end))