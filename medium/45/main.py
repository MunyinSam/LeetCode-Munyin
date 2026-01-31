class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)

        dp = [0]

        for i in range(n):
            dp.append(9999999)

        for i in range(n):
            jump = nums[i]

            for j in range(i + 1, jump + i + 1):
                if j > n:
                    break
                if dp[j] > dp[i] + 1:
                    dp[j] = dp[i] + 1
        
        return dp[n-1]