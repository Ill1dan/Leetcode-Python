def sortArray(nums):
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

    return mergeSort(nums)



nums = [5, 1, 1, 2, 0, 0]
print(sortArray(nums))