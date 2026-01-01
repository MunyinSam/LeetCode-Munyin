class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subsets = [[]]

        for n in nums:
            new_subset = []
            

s = Solution()
answer = s.subsets([1,2,3])
print(answer)

