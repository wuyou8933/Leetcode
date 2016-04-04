class Solution(object):
    def majorityElement(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        dict={}
        for i in nums:
            if dict.has_key(i):
                dict[i]+=1
                if dict[i]>len(nums)/2:
                    return i
            else:
                dict[i]=1
                if dict[i]>len(nums)/2:
                    return i