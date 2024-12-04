def canMakeSubsequence(str1, str2):
    i = 0
    subsequence_found = 0

    for j in str2:
        while i < len(str1):
            if str1[i] == j or chr((((ord(str1[i]) + 1) - 97) % 26) + 97) == j:
                subsequence_found += 1
                i += 1
                break
            i += 1

    if subsequence_found == len(str2):
        return True
    return False


str1 = "c"
str2 = "b"
print(canMakeSubsequence(str1, str2))