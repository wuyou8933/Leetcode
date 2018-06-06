class Solution(object):
    def isValid(self, s):
        """
            :type s: str
            :rtype: bool
            """
       stack = []
    """
    :type s: str
    :rtype: bool
    """
        for char in s:
            print stack
            # import pdb;pdb.set_trace()
            if char in "([{":
                stack.append(char)
            elif not stack:
                return False
            elif char == ")" and stack.pop() == "(":
                continue
            elif char == "]" and stack.pop() == "[":
                continue
            elif char == "}" and stack.pop() == "{":
                continue
            else:
                return False
        return not stack