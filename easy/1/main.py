class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        c_idx = 0

        while True:
            for i in range(c_idx + 1, len(nums)):
                if nums[c_idx] + nums[i] == target:
                    return [c_idx, i]
            c_idx += 1
        return


s = Solution()

nums = [3,2,4]
target = 6

print(s.twoSum(nums, target))