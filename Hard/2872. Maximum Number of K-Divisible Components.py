from collections import defaultdict


def maxKDivisibleComponents(n, edges, values, k):
    adj = defaultdict(list)

    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    res = 0

    def dfs(cur, parent):
        total = values[cur]

        for child in adj[cur]:
            if child != parent:
                total += dfs(child, cur)

        if total % k == 0:
            nonlocal res
            res += 1
        return total

    dfs(0, -1)

    return res

n = 5
edges = [[0, 2], [1, 2], [1, 3], [2, 4]]
values = [1, 8, 1, 4, 4]
k = 6
print(maxKDivisibleComponents(n, edges, values, k))