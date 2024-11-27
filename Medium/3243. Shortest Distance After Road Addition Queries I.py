from heapq import heappop, heappush

def shortestDistanceAfterQueries(n, queries):
    def adjacencyList(v, edges):
        dict = {i: [] for i in range(v)}

        for x, y in edges:
            dict[x].append((y, 1))

        return dict

    def dijkstra(graph, source):
        distances = {i: float('inf') for i in range(n)}
        distances[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_vertex = heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(priority_queue, (distance, neighbor))

        return distances

    edges = [[x, x + 1] for x in range(n - 1)]
    res = []

    for i in range(len(queries)):
        edges.append(queries[i])
        graph = adjacencyList(n, edges)
        distance = dijkstra(graph, 0)
        res.append(distance[n - 1])

    return res

n = 5
queries = [[2,4],[0,2],[0,4]]
print(shortestDistanceAfterQueries(n, queries))