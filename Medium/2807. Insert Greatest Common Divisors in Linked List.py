import math


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        tail1, tail2 = head, head.next

        while tail2:
            node_gcd = math.gcd(tail1.val, tail2.val)

            node = ListNode(node_gcd)
            tail1.next = node
            node.next = tail2
            tail1 = tail2
            tail2 = tail2.next

        return head


head = [18, 6, 10, 3]