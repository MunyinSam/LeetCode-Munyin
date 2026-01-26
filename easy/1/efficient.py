class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        h_map = {}

        for i, num in enumerate(nums):
            diff = target - num 
            if diff in h_map:
                return [h_map[diff], i]
            h_map[num] = i
        return

s = Solution()

nums = [3,2,4]
target = 6

print(s.twoSum(nums, target))