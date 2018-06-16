"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    """Traverse array of numbers, check if the difference between target value and current entry in the array is present
    in hashtable. If not, add it to hashtable along with its index and continue on. If it is, return the index of the 
    current number and the index of the diff from the hash table.
    """
    ht = {}
    for i in range(len(nums)):
        n = nums[i]
        if target - n in ht:
            return [ht[target - n], i]
        else:
            ht[n] = i


def main():
    val = twoSum([-3, 1, 5, 3], 0)
    print (val)

if __name__ == "__main__":
    main()