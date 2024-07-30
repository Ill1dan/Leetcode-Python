def minimumDeletions(s):
    stack = []
    deleted = 0

    for i in s:
        if stack and stack[-1] == "b" and i == "a":
            stack.pop()
            deleted += 1
        else:
            stack.append(i)

    return deleted

s = "bbaaaaabb"
print(minimumDeletions(s))