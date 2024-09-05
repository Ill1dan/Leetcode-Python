def missingRolls(rolls, mean, n):
    n_sum = sum(rolls)
    m_sum = mean * (n + len(rolls)) - n_sum

    if m_sum > 6 * n or m_sum < n:
        return []

    res = [m_sum // n] * n

    for i in range(m_sum % n):
        res[i] += 1

    return res


rolls = [3, 2, 4, 3]
mean = 4
n = 2
print(missingRolls(rolls, mean, n))