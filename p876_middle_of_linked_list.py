# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import math


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return None

        if head.next == None:
            return head

        count = 0
        curr = head
        while (curr):
            curr = curr.next
            count += 1

        mid = count // 2
        curr = head
        count = 0
        while (curr):
            if count == mid:
                return curr
            else:
                count += 1
                curr = curr.next