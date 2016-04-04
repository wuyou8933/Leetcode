class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
            :type s: str
            :rtype: int
            """
        L, res, lastAppear = -1, 0, [-1] * 128
        for R, char in enumerate(s):
            pos = ord(char)
            if lastAppear[pos] > L:
                L = lastAppear[pos]
            else:
                res = max(res, R - L)
            lastAppear[pos] = R
        return res