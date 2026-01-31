class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * 31

        dp[0], dp[1] = 0, 1

        for i in range(n - 1):
            dp[i + 2] = dp[i] + dp[i + 1]

        return dp[n]