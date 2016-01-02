import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace = True)
df = pd.DataFrame(loansData)

intrates = df['Interest.Rate'].map(lambda x: round(float(x.strip('%')), 4))
loanlength = df['Loan.Length'].map(lambda x: int(x.strip(' months')))
FICOscores = df['FICO.Range'].map(lambda x: x.split("-"))
FICOscore1 = FICOscores.map(lambda x: int(x[0]))
FICOscore2 = FICOscores.map(lambda x: int(x[1]))
df['Interest.Rate'] = intrates
df['Loan.Length'] = loanlength
df['FICO.Score'] = FICOscore1

intrate = df['Interest.Rate']
loanamt = df['Amount.Requested']
fico = df['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print(f.summary())