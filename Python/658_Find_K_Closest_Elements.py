from heapq import *
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        result = []
        for i in arr:
            if len(result) < k:
                heappush(result,(-abs(i-x),i))
            else:
                temp = heappop(result)
                if temp[0] < -abs(i-x):
                    heappush(result,(-abs(i-x),i))             
                else:
                    heappush(result,temp)
        return sorted([x[1] for x in result])
