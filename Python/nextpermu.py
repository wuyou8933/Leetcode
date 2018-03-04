def nextPermutation(nums):
    i = len(nums)-1
    while i > 0:
        if nums[i] > nums[i-1]:
            for j in xrange(len(nums)-1, 0, -1):
                if nums[j] > nums[i-1]:
                    nums[j], nums[i-1] = nums[i-1], nums[j]
                    break
            break
        i -= 1
    nums[i:] = nums[i:][::-1]

nums = [3,2,1]
print nextPermutation(nums)
print nums 
# print nums