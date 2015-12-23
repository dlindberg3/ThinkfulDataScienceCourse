with open('ruraldata/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
	for line in inputFile:
		line = line.rstrip().split(',')
		print(len(line))