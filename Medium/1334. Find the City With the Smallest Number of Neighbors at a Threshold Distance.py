from heapq import heapify, heappop

def findTheCity(n, edges, distanceThreshold):
    def adjacencyList(v, list):
        dict = {}

        for x in range(v + 1):
            dict[x] = []

        for z in list:
            dict[z[0]].append((z[1], z[2]))

        return dict


    def find_least(list):
        new_list = []

        for x in range(len(list)):
            if list[x][1] != 1:
                new_list.append(list[x])

        heapify(new_list)
        vertex = heappop(new_list)

        for y in range(len(list)):
            if list[y] == vertex:
                return y


    def dijkstra(graph, source, dijkstra_distance):
        flag = False
        for y in dijkstra_distance:
            if y[1] == 0:
                flag = True

        if flag == False:
            return

        for x in graph[source]:
            if dijkstra_distance[x[0]][1] != 1 and dijkstra_distance[x[0]][0] > x[1]:
                if x[1] + dijkstra_distance[source][0] < dijkstra_distance[x[0]][0]:
                    dijkstra_distance[x[0]][0] = x[1] + dijkstra_distance[source][0]

        least = find_least(dijkstra_distance)
        dijkstra_distance[least][1] = 1
        dijkstra(graph, least, dijkstra_distance)


    for x in range(len(edges)):
        edges.append([edges[x][1], edges[x][0], edges[x][2]])

    graph = adjacencyList(n - 1, edges)
    distances = []

    for i in range(n):
        dijkstra_distance = []
        for y in range(n):
            dijkstra_distance.append([float("inf"), 0])
        dijkstra_distance[i] = [0, 1]
        dijkstra(graph, i, dijkstra_distance)
        distances.append(dijkstra_distance)

    valid_distance = {}
    min_dis = float("inf")
    for j in range(len(distances)):
        for k in range(len(distances[j])):
            if 0 < distances[j][k][0] <= distanceThreshold:
                if j in valid_distance:
                    valid_distance[j].append(k)
                else:
                    valid_distance[j] = [k]

        if j not in valid_distance:
            valid_distance[j] = []

        if len(valid_distance[j]) <= min_dis:
            min_dis = len(valid_distance[j])
            output = j


    return output


n = 6
edges = [[0, 3, 7], [2, 4, 1], [0, 1, 5], [2, 3, 10], [1, 3, 6], [1, 2, 1]]
distanceThreshold = 417
print(findTheCity(n, edges, distanceThreshold))