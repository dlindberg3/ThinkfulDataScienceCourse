#with open('ruraldata/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
#    for line in inputFile:
#        line = line.rstrip().split(',')
#        print(line)
		
with open('ruraldata/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
    for line in inputFile:
        line = line.rstrip().split(',')
        print(len(line))

import csv

with open('ruraldata/lecz-urban-rural-population-land-area-estimates_codebook.csv','r') as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        print(len(line))