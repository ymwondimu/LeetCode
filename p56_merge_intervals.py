# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if len(intervals) == 0:
            return []

        intervals = sorted(intervals, key=lambda x: x.start)

        stack = []
        stack.append(intervals[0])

        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            prev_interval = stack.pop()

            if prev_interval.end >= curr_interval.start:
                prev_interval.end = max(curr_interval.end, prev_interval.end)
                stack.append(prev_interval)
            else:
                stack.append(prev_interval)
                stack.append(curr_interval)

        return stack