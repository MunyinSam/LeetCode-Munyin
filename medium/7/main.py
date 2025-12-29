class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 1
        if x < 0:
            negative = -1
            x *= -1
        r = 0
        while x > 0:
            r *= 10
            r += x % 10
            x //= 10
        return r * negative
            

s = Solution()
answer = s.reverse(120)
print(answer)