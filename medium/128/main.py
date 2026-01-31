class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = {} # values consecutive
        

        for i, num in enumerate(1, nums):
            if num in dp:
                continue
            

            dp[num] = Node(num)
            


nums = [1, 0]
s = Solution()
print(s.longestConsecutive(nums))