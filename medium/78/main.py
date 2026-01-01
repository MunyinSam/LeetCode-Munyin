class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subsets = []

        def helper(idx, cur_subset=[]):

            print(idx, cur_subset)

            if idx == len(nums):
                subsets.append(list(cur_subset))
                return

            # include
            cur_subset.append(nums[idx])
            helper(idx + 1, cur_subset)

            # not include
            cur_subset.pop()
            helper(idx + 1, cur_subset)



        helper(0, []) # get next
        return subsets

s = Solution()
answer = s.subsets([1,2,3])
print(answer)

