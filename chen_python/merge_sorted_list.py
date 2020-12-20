#merge sorted list
def Mergesortlist(arr1, m, arr2, n):
	p1 = m - 1
	p2 = n - 1
	p = m + n - 1
	while p1 >= 0 and p2 >= 0:
		if arr1[p1] < arr2[p2]:
			arr1[p] = arr2[p2]
			p2 -= 1
			p -= 1
		else:
			arr1[p] = arr1[p1]
			p1 -= 1
			p -= 1
	while p2 >= 0:
		arr1[p] = arr2[p2]
		p2 -= 1
		p -= 1
	return arr1
arr1 = [1,2,3,0,0,0]
m = 3
arr2 = [2,4,5]
n = 3
print(Mergesortlist(arr1, m, arr2, n))