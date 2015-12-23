import collections 
pop2010 = collections.defaultdict(int)
pop2100 = collections.defaultdict(int)
area = collections.defaultdict(int)
pct_chg = collections.defaultdict(float)
dens2010 = collections.defaultdict(float)
with open('ruraldata/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
	header = next(inputFile)
	for line in inputFile:
		line = line.rstrip().split(',')
		for i in range(3,8):
			line[i] = int(line[i])
		if line[1] == 'Total National Population':
			pop2010[line[0]] += line[5]
			pop2100[line[0]] += line[6]
			area[line[0]] += line[7]
			pct_chg[line[0]] = (float(pop2100[line[0]]) / float(pop2010[line[0]]) - 1) * 100
			dens2010[line[0]] = float(pop2010[line[0]]) / float(area[line[0]])
# print(pop2010)
# print(pop2100)
print(dens2010)

with open('national_population.csv', 'w') as outputFile:
	outputFile.write('continent,dens2010\n')
	for k,v in dens2010.iteritems():
		outputFile.write(k + ',' + str(v) + '\n')