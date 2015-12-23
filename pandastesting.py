import pandas as pd 

input_dataframe = pd.read_csv('ruraldata/lecz-urban-rural-population-land-area-estimates_country-90m.csv')

unique_continents = []
for line in input_dataframe['Continent']:
	if not(line in unique_continents):
		unique_continents.append(line)

for line in unique_continents:
	print(line)