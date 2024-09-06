class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def modifiedList(self, nums, head):
        nums = set(nums)
        valid = []

        tail = head
        while tail:
            if tail.val not in nums:
                valid.append(tail.val)

            tail = tail.next

        head = ListNode(valid[0])
        tail = head

        for i in range(1, len(valid) + 1):
            node = ListNode(valid[i])
            tail.next = node
            tail = node

        return head


nums = [1, 2, 3]
head = [1, 2, 3, 4, 5]


