class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
            else:
                continue
        
        return profit

s = Solution()
prices = [1,5,3,100]
print(s.maxProfit(prices))
