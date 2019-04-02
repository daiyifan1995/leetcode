# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = l1
        p = 0
        while l1 != None and l2 != None:
            l1.val = l1.val + l2.val + p
            if l1.val < 10:
                p = 0
            else:
                l1.val = l1.val - 10
                p = 1
            f1 = l1
            l1 = l1.next
            l2 = l2.next
        if l1 == None:
            f1.next = l2
            while l2 != None:
                l2.val = l2.val + p
                if l2.val >= 10:
                    l2.val = l2.val - 10
                    p = 1
                else:
                    p = 0
                f1 = l2
                l2 = l2.next
        else:
            while l1 != None:
                l1.val = l1.val + p
                if l1.val >= 10:
                    l1.val = l1.val - 10
                    p = 1
                else:
                    p = 0
                f1 = l1
                l1 = l1.next
        if p == 1:
            f1.next = ListNode(1)

        return result

