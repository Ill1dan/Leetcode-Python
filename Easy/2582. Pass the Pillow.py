def passThePillow(n, time):
    from_top = True

    while time >= n:
        from_top = not from_top
        time -= n - 1

    if from_top:
        return 1 + time
    else:
        return n - time



print(passThePillow(7, 14))