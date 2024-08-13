def combinationSum2(candidates, target):
    res = []
    candidates.sort()

    def backtrack(i, current, total):
        if total == target:
            res.append(current.copy())
            return
        if total > target or i == len(candidates):
            return

        current.append(candidates[i])
        backtrack(i + 1, current, total + candidates[i])
        current.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1
        backtrack(i + 1, current, total)

    backtrack(0, [], 0)

    return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))