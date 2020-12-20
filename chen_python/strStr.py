#strStr
def strStr(input, scr):
	if input == scr:
		return 0
	m = len(input)
	n = len(scr)
	if m == 0 and n == 0:
		return 0
	for i in range(0, m -n +1):
		if input[i:i+n] == scr:
			return i
	return -1
input = "hello"
scr = "ll"
print(strStr(input,scr))