def lemonadeChange(bills):
    frequency = {5: 0, 10: 0}

    for i in bills:
        if i == 5:
            frequency[i] += 1
        elif i == 10:
            frequency[i] += 1
            if frequency[5] == 0:
                return False
            frequency[5] -= 1
        else:
            if frequency[5] > 0 and frequency[10] > 0:
                frequency[10] -= 1
                frequency[5] -= 1
            elif frequency[5] > 2:
                frequency[5] -= 3
            else:
                return False

    return True


bills = [5, 5, 10, 10, 20]
print(lemonadeChange(bills))