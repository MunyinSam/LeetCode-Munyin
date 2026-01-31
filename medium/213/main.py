class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            return nums[0]

        # case เอาหัว
        dp = [0] * 1000

        for i in range(n - 2, -1, -1):
            
            if nums[i] + dp[i + 2] > dp[i + 1]:
                dp[i] = nums[i] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]

        first_case = max(dp[0], dp[1])

        # case เอาหาง
        dp = [0] * 1000

        for i in range(n - 1, 0, -1):
            
            if nums[i] + dp[i + 2] > dp[i + 1]:
                dp[i] = nums[i] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]

        second_case = max(dp[0], dp[1])

        # case ไม่หัวหาง
        dp = [0] * 1000

        for i in range(n - 2, 0, -1):
            
            if nums[i] + dp[i + 2] > dp[i + 1]:
                dp[i] = nums[i] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]
        third_case = max(dp[0], dp[1])

        return max(first_case, second_case, third_case)
