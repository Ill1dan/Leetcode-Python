from collections import defaultdict


def queryResults(limit, queries):
    res = []
    curr = 0
    distinct_colors = set()
    colors = defaultdict(int)
    balls = {}

    for x, y in queries:
        if x in balls:
            prev_color = balls[x]
            if prev_color in distinct_colors:
                colors[prev_color] -= 1
                if colors[prev_color] == 0:
                    distinct_colors.remove(prev_color)
                    curr -= 1

            balls[x] = y

        else:
            balls[x] = y

        if colors[y] == 0:
            distinct_colors.add(y)
            curr += 1
        colors[y] += 1

        res.append(curr)

    return res


limit = 1
queries = [[0,1],[0,4],[0,4],[0,1],[1,2]]
print(queryResults(limit, queries))