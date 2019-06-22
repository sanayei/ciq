# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None




def add(n1, n2):
    head = ListNode(0)
    cur = head
    s = 0
    while n1 or n2:
        (v1, n1) = (n1.val, n1.next) if n1 else (0, n1)
        (v2, n2) = (n2.val, n2.next) if n2 else (0, n2)
        s = v1 + v2 + s
        r = s % 10
        s = s // 10
        cur.next = ListNode(r)
        cur = cur.next
    if s > 0:
        cur.next = ListNode(s)
    return head.next



if __name__ == '__main__':
    n1 = ListNode(2)
    n1.next = ListNode(4)
    n1.next.next = ListNode(3)

    n2 = ListNode(5)
    n2.next = ListNode(6)
    n2.next.next = ListNode(4)

    n = add(n1, n2)
    print('done')