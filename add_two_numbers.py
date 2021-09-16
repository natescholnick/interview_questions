# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    head = None
    node_in_chain = None
    carry = 0

    while l1 is not None or l2 is not None:
        digit_sum = carry

        if l1 is not None:
            digit_sum += l1.val
            l1 = l1.next

        if l2 is not None:
            digit_sum += l2.val
            l2 = l2.next

        carry = digit_sum // 10
        node = ListNode(digit_sum % 10)

        if node_in_chain is None:
            node_in_chain = head = node
        else:
            node_in_chain.next = node
            node_in_chain = node_in_chain.next

    if carry:
        node_in_chain.next = ListNode(carry)

    return head


a = ListNode(4)
a.next = ListNode(1)
a.next.next = ListNode(3)

b = ListNode(2)
b.next = ListNode(4)

addTwoNumbers(a, b)  # outputs [6, 5, 3]
