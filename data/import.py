import csv, re
from os import walk
filenames = []
for (dirpath, dirnames, filenames) in walk('/Users/jouanchen/Desktop/data/'):
	filenames.append(filenames)
for filename in filenames:
	if 'csv' in filename:
		with open('/Users/jouanchen/Desktop/data/{}'.format(filename), 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
			list =[]
			try:
				for row in spamreader:
					list.append(row) 
			except:
				pass
			j = 1
			i = 2
			while j < len(list):
				try:
				# print list[j][len(list[j])-10]
					while i < len(list[j])-1:
						if '(' in list[j][i].split(',')[0]:
							print "{},{}".format(list[j][i][1:], list[j][i+1])
						elif re.search('[a-zA-Z]', list[j][i]) is not None or re.search('[a-zA-Z]', list[j][i+1]) is not None:
							i += 2
						else:
							# print list[j][i+1],len(list[j])
							print "{},{}".format(list[j][i].split(',')[1], list[j][i+1])
						i += 2
				except:
					print "ERROR with {} and {} TRUE:{} in filename {}".format(list[j][i], list[j][i+1], 'test', filename)
					j += 1
					print "{},{}"
				
			# 	#for debug use
				
			# 	# while i < len(list[1])-1:
			# 		# print list[1][i].split(',')[0]
			# 		# i += 2
				j += 1