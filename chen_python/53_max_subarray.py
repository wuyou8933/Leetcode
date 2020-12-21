# def maxSubArray(nums):
	
# 	if len(nums) == 0:
# 		return
# 	max_num = curr = nums[0]
# 	for i in range(1,len(nums)):
# 		curr = max(curr+nums[i], curr)
# 		max_num = max(max_num, curr)
# 	return max_num
# a = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(a))



def maxSubArray(nums):
    if len(nums) == 0:
        return
    
    max_num = curr = nums[0]
    for i in range(1,len(nums)):
        
        curr = max(nums[i], nums[i]+curr)
        max_num = max(curr, max_num)
    return max_num

a = [1,1,1,1]
print(maxSubArray(a))