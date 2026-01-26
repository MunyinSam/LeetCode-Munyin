class Solution:

    def subsetsWithDup(self, nums):

        res = []
        nums.sort()

        def helper(idx, cur):

            if idx == len(nums):
                res.append(list(cur))
                return

            # include
            cur.append(nums[idx])
            helper(idx + 1, cur)
            cur.pop()
            # exclude
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            helper(idx + 1, cur)

        helper(0, [])
        
        return res


s = Solution()
nums = [1, 2, 2]
print(s.subsetsWithDup(nums))        