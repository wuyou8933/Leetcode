def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums:
        return []
    tempMax = max(nums[:k])
    res = []
    res.append(tempMax)
    
    for i in range(k, len(nums)):
        if nums[i] > tempMax:
            tempMax = nums[i]
        elif tempMax != nums[i-k]:
            tempMax = max(tempMax, nums[i])
        else:
            tempMax = max(nums[i-k+1:i+1])
        res.append(tempMax)
    return res