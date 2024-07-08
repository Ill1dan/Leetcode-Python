class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

def addTwoNumbers(l1, l2):
    head = ListNode()
    h3 = head

    sum = carry = 0

    while l1 or l2 or carry:
        sum = carry

        if l1:
            sum += l1.val
            l1 = l1.next

        if l2:
            sum += l2.val
            l2 = l2.next

        total = sum % 10
        carry = sum // 10

        h3.next = ListNode(total)
        h3 = h3.next

    return head.next

print(addTwoNumbers(l1,l2))