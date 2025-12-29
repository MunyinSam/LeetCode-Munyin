class Solution(object):

    def __init__(self):
        self.dic = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

    def toNum(self, str):
        total = 0
        for i, value in enumerate(str[::-1]):
            total += self.dic[value] * pow(10, i)
        
        return total

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        return str(self.toNum(num1) * self.toNum(num2))
        
s = Solution()
answer = s.multiply("123", "456")
print(answer)