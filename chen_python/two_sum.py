# two sum
#list[] target return index
def twoSum(input, target):
	input.sort()
	p1 = 0
	p2 = len(input) - 1
	while p2 > p1:
		if input[p1] + input[p2] == target:
			return (p1, p2)
		elif input[p1] + input[p2] > target:
			p2 -= 1
		elif input[p1] + input[p2] < target:
			p1 += 1
	return -1

input = [1,2,3,4,5]
target = 8
print(twoSum(input, target))




