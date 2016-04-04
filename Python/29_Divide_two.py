class Solution(object):
    def divide(self, dividend, divisor):
        """
            :type dividend: int
            :type divisor: int
            :rtype: int
            """
        if dividend==-2147483648 and divisor==-1 or divisor==0:return 2147483647
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0; count = 0; res = 0
        a = abs(dividend); b = abs(divisor)
        while a >= b:
            sum = b
            count = 1
            while sum<<1<=a:
                sum <<=1
                count <<=1
            a -= sum
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        return res