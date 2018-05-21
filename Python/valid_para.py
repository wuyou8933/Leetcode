def para(ps):
	list_p =[]
	for s in ps:
		if s in "[({":
			list_p.append(s)
		elif not list_p:
			return False
		else:
			if s == ")" and "(" in list_p:
				list_p.remove("(")
				continue
			if s == "]" and "[" in list_p:
				list_p.remove("[")
				continue
			if s == "}" and "{" in list_p:
				list_p.remove("{")
				continue
			else:
				return False
	return not list_p

print para("()[]")