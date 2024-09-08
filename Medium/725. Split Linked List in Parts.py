class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def splitListToParts(self, head, k):
        tail = head
        length = 0

        while tail:
            length += 1
            tail = tail.next

        res = [length // k] * k
        for i in range(length % k):
            res[i] += 1

        if length // k == 0:
            for i in range(length % k, k):
                res[i] = None

        tail = head
        temp = head
        count = 0
        i = 0

        while tail:
            count += 1
            next_node = tail.next

            if count == res[i]:
                tail.next = None
                res[i] = temp
                temp = next_node
                count = 0
                i += 1

            tail = next_node

        return res


head = [1, 2, 3]
k = 5