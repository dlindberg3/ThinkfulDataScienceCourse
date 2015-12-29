import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns = column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print('The mean household spending on alcohol is ' + str(round(df['Alcohol'].mean(), 2)))
print('The mean household spending on alcohol is ' + str(round(df['Alcohol'].median(), 2)))
print('The mode of the household spending on alcohol is ' + str(round(stats.mode(df['Alcohol'])[0][0], 2)))
print('The range of the household spending on alcohol is ' + str(round(max(df['Alcohol']) - min(df['Alcohol']), 2)))
print('The standard deviation of the household spending on alcohol is ' + str(round(df['Alcohol'].std(), 3)))
print('The variance of the household spending on alcohol is ' + str(round(df['Alcohol'].var(), 3)))
print('\n')
print('The mean household spending on tobacco is ' + str(round(df['Tobacco'].mean(), 2)))
print('The mean household spending on tobacco is ' + str(round(df['Tobacco'].median(), 2)))
print('The mode of the household spending on tobacco is ' + str(round(stats.mode(df['Tobacco'])[0][0], 2)))
print('The range of the household spending on tobacco is ' + str(round(max(df['Tobacco']) - min(df['Tobacco']), 2)))
print('The standard deviation of the household spending on tobacco is ' + str(round(df['Tobacco'].std(), 3)))
print('The variance of the household spending on tobacco is ' + str(round(df['Tobacco'].var(), 3)))
