class Solution(object):
    def reverse(self, x):
        """
            :type x: int
            :rtype: int
            """
        sign=1
        if x<0:sign=-1
        x=abs(x)
        result=0
        while x>=1:
            result=result*10+x%10
            x/=10
        if -2147483649<=result*sign<=2147483648:
            return result*sign
        else:
            return 0