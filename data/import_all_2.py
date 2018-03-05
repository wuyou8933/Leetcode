import csv, re
from os import walk

def hasNumbers(inputString):
     return bool(re.search(r'\d', inputString))

filenames = []
for (dirpath, dirnames, filenames) in walk('/Users/jouanchen/Desktop/Myanmar'):
	filenames.append(filenames)
output = open("/Users/jouanchen/Desktop/Myanmarall_multi.csv", 'w')
output.write("WKT,Name\n")
for filename in filenames:
	if 'csv' in filename and '.swp' not in filename:
		f = open("/Users/youwu/Desktop/Myanmar{}".format(filename),"rb")
		input = f.read() 
		i = 1
		temp = ""
		while i < len(input.split("\"")): 
			if hasNumbers(str(input.split("\"")[i])):
				temp += str(input.split("\"")[i])
			i += 2
		if temp.find("LINESTRING Z ") != -1:
			temp1 = "\"MULTILINESTRING " + temp.replace("LINESTRING Z ", "(").replace(" 0,",",").replace(" 0)",")") + ")\",{}\n".format(str(filename).replace(".csv",""))
		else:
			temp1 = "\"MULTIPOINT " + temp.replace("POINT Z ", "(").replace(" 0,",",").replace(" 0)",")") + ")\",{}\n".format(str(filename).replace(".csv",""))
		# print filenames
		output.write(temp1.replace(")((","),("))
output.close()
# print temp.find("LINESTRING Z ", 50)
# print temp