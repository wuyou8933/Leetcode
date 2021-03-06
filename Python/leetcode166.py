def fractionToDecimal(numerator, denominator):
    sign = '-' if numerator * denominator < 0 else ''
    head, remainder = divmod(abs(numerator), abs(denominator))
    tail, seen = '', {}
    while remainder != 0:
        if remainder in seen:
            tail = '(' + tail[seen[remainder]:] + ')'
            break
        seen[remainder] = len(tail)
        digit, remainder = divmod( remainder*10, abs(denominator) )
        tail+=str(digit)
    return sign + str(head) + (tail and '.' + tail)

print fractionToDecimal(10000,5)