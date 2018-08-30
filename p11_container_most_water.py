class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left_index = 0
        right_index = len(height) - 1
        max_area = -1

        while (left_index < right_index):
            new_area = min(height[left_index], height[right_index]) * (right_index - left_index)
            if new_area > max_area:
                max_area = new_area

            if height[left_index] > height[right_index]:
                right_index -= 1
            else:
                left_index += 1

        return max_area