from collections import deque


def secondMinimum(n, edges, time, change):
    graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([(1, 1)])
    distance1 = [-1] * (n + 1)
    distance2 = [-1] * (n + 1)
    distance1[1] = 0

    while queue:
        x, fre = queue.popleft()
        t = distance1[x] if fre == 1 else distance2[x]
        if (t // change) % 2:
            t = change * (t // change + 1) + time
        else:
            t += time

        for y in graph[x]:
            if distance1[y] == -1:
                distance1[y] = t
                queue.append((y, 1))
            elif distance2[y] == -1 and distance1[y] != t:
                if y == n:
                    return t
                distance2[y] = t
                queue.append((y, 2))

    return 0


n = 2
edges = [[1, 2]]
time = 3
change = 2

print(secondMinimum(n, edges, time, change))