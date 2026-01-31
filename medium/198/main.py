class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [0] * 1000

        n = len(nums)

        for i in range(n - 1, -1, -1):
            
            if nums[i] + dp[i + 2] > dp[i + 1]:
                dp[i] = nums[i] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]
        
        return max(dp[0], dp[1])

