from collections import defaultdict


def queryResults(limit, queries):
    res = []
    colors = defaultdict(int)
    cnt = 0

    for i in queries:
        if i[0] not in colors:
            cnt += 1
            colors[i[0]] = i[1]
        else:
            if colors[i[0]] != i[1]:
                cnt += 1
                colors[i[0]] = i[1]

        res.append(cnt)

    return res


limit = 4
queries = [[1,4],[2,5],[1,3],[3,4]]
print(queryResults(limit, queries))