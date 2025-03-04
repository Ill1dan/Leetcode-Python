def checkPowersOfThree(n):
    i = 0
    while 3 ** (i + 1) <= n:
        i += 1

    while i >= 0:
        power = 3 ** i
        if power <= n:
            n -= power
        if power <= n:
            return False
        i -= 1

    return n == 0

n = 12
print(checkPowersOfThree(n))