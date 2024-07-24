def sortJumbled(mapping, nums):
    dict = {}
    for x in nums:
        num = str(x)
        val = ""
        for y in num:
            val += str(mapping[int(y)])
        val = int(val)
        if val in dict:
            dict[val].append(x)
        else:
            dict[val] = [x]

    def merge(a, b):
        new_list = [0] * (len(a) + len(b))

        i = 0
        j = 0

        for x in range(len(new_list)):
            if i == len(a) and j != len(b):
                new_list[x] = int(b[j])
                j += 1
            elif j == len(b) and i != len(a):
                new_list[x] = int(a[i])
                i += 1
            elif int(a[i]) < int(b[j]):
                new_list[x] = int(a[i])
                i += 1
            else:
                new_list[x] = int(b[j])
                j += 1

        return new_list

    def mergeSort(arr):
        if len(arr) == 1:
            return arr
        else:
            mid = len(arr) // 2
            l = mergeSort(arr[:mid])
            r = mergeSort(arr[mid:])
            return merge(l, r)


    arr = mergeSort(list(dict))

    output = []
    for i in arr:
        val = dict[i]
        for j in val:
            output.append(j)

    return output


mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
nums = [991, 338, 38]
print(sortJumbled(mapping, nums))