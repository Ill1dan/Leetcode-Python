def minOperations(logs):
    steps_req = 0

    for x in logs:
        if x == "../":
            if steps_req > 0:
                steps_req -= 1
        elif x == "./":
            steps_req += 0
        else:
            steps_req += 1

    return steps_req



arr = ["d1/","d2/","./","d3/","../","d31/"]
print(minOperations(arr))