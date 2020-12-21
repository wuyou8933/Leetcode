#zigzag matrix
def Zigzag(matrix):
	row = len(matrix)
	col = len(matrix[0])
	d = dict()
	ans = []
	for i in range(row):
		for j in range(col):
			if i+j not in d:
				d[i+j] = [matrix[i][j]]
			else:
				d[i+j].append(matrix[i][j])
	for entry in d.items():
		if entry[0] % 2 == 0:
			ans.extend(entry[1][::-1])
		else:
			ans.extend(entry[1])
	return ans

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Zigzag(matrix))