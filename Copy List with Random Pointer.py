#拷贝带有随机链表的链表

#使用字典将新链表的val与地址储存下来，根据原链表的random指针的val进行赋值
"""
# Definition for a Node."""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        nodeDict = dict()
        if head != None:
            root = Node(head.val, head.next, head.random)
            nodeDict[root.val] = root
        else:
            return None

        res = root
        inputHead = head

        head = head.next

        while head != None:
            root.next = Node(head.val, head.next, None)
            head = head.next
            root = root.next
            nodeDict[root.val] = root

        root = res
        head = inputHead
        while root != None and head != None:
            if head.random != None:
                root.random = nodeDict[head.random.val]
            else:
                root.random = None
            head = head.next
            root = root.next

        return res
