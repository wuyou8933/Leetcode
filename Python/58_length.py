class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = s.split()
        if temp:
            return len(temp[-1])
        else:
            return 0