with open('ex6207.csv', 'rU') as inputfile:
	header = next(inputfile)
	for line in inputfile:
		line = line.rstrip().split(',')
		print(line)
		

		
