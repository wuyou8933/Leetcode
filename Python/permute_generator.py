def helper(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 0:
        yield ()
    if len(nums) == 1:
        yield (nums[0],)
    for i in range(len(nums)):
        for j in helper(nums[:i]+nums[i+1:]):
            yield (nums[i],)+j
            
def permute(nums):
    return [list(t) for t in set(helper(nums))]

print permute([1,2,3])