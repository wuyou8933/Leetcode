# two sum hashtable
def twoSum(input,target):
	d = dict()
	for i in range(len(input)):
		comp = target - input[i]
		if comp not in d:
			d[input[i]] = i
		else:
			return (d[comp], i)
input = [1,2,3,4,5]
target = 8
print(twoSum(input, target))
