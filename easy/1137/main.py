class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * 38

        if n == 0:
            return 0
        if n == 1:
            return 1

        dp[0], dp[1], dp[2] = 0, 1, 1

        for i in range(n - 2):
            dp[i + 3] = dp[i] + dp[i + 1] + dp[i + 2]

        return dp[n]