# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

from collections import defaultdict


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        d = defaultdict(lambda: RandomListNode(0))
        d[None] = None

        cur = head
        while (cur):
            d[cur].label = cur.label
            d[cur].next = d[cur.next]
            d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]


