def strStr(haystack, needle):
	k = len(haystack)
	j = len(needle)
	if k == 0 and j == 0:
		return 0
	if k == 0 and j != 0:
		return -1
	if haystack == needle:
		return 0
	for i in range(0, k - j + 1):
		if needle == heystack[i:i+j]:
			return i
	
	return -1
heystack = ""
needle = "ll"
print(strStr(heystack, needle))