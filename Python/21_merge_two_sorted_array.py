def merge_two(a,b):
	while a and b:
		if a.val>b.val:
			a,b=b,a
			a.next = merge_two(a.next,b)
		return a or b