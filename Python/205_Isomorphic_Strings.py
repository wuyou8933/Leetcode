class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dt = dict()
        for char_s, char_t in zip(s,t):
            if char_s not in char_dt:
                if  char_t not in char_dt.values():
                    char_dt[char_s] = char_t
                else:
                    return False
            else:
                if char_dt[char_s] == char_t:
                    pass
                else:
                    return False
        return True