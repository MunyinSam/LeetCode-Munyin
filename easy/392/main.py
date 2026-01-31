class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = 0
        found = 0
        for i in range(len(s)):
            for j in range(idx, len(t)):
                if s[i] == t[j]:
                    idx = j + 1
                    found += 1
                    break
        return found == len(s)