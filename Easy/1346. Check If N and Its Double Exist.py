def checkIfExist(arr):
    visited = set()
    for i in arr:
        if i * 2 in visited or (i % 2 == 0 and i // 2 in visited):
            return True
        visited.add(i)
    return False


arr = [-2,0,10,-19,4,6,-8]
print(checkIfExist(arr))