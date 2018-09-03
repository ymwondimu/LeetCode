class MinNode(object):
    def __init__(self, val):
        self.val = val
        self.min = None


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        node = MinNode(x)
        if len(self.stack) == 0:
            node.min = node.val
        else:
            if node.val > self.stack[-1].min:
                node.min = self.stack[-1].min
            else:
                node.min = node.val
        # print ("APPENDING")
        # print ("VAL: " + str(node.val) + " MIN: " + str(node.min))
        self.stack.append(node)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) > 0:
            # print ("POPPING")
            node = self.stack.pop()
            # print (node.val)
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1].val
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """

        if len(self.stack) > 0:
            return self.stack[-1].min
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()