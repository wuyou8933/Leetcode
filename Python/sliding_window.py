def maxSlidingWindow(nums, k):
	result = []
	for i in range(len(nums)-k+1):
		result.append(max(nums[i:i+k]))
	return result

print maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)