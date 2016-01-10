import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import statsmodels.formula.api as smf

loansData = pd.read_csv('LoanStats3a.csv')
loansData2 = loansData[['int_rate','home_ownership','annual_inc']]
loansData2.dropna(inplace = True)
df = pd.DataFrame(loansData2)

intrate = df['int_rate'].map(lambda x: round(float(x.strip('%')), 4))
anninc = df['annual_inc']
homeown = df['home_ownership']

# Simple Linear Regression of Interest Rate versus Annual Income
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(anninc).transpose()

X = sm.add_constant(x1)

model1 = sm.OLS(y,X)
f1 = model1.fit()

print(f1.summary())

# Multiple Linear Regression with Categorical Data
df2 = pd.DataFrame(np.column_stack([intrate,anninc,homeown]), columns = ['intrate','anninc','homeown'])

# Make dummy variables
homeown_dummies = pd.get_dummies(df2.homeown, prefix='Homeown').iloc[:, 1:]
df2 = pd.concat([df2, homeown_dummies], axis=1)
print(df2.head())

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(anninc).transpose()
x2 = np.matrix(df2.Homeown_NONE).transpose()
x3 = np.matrix(df2.Homeown_OTHER).transpose()
x4 = np.matrix(df2.Homeown_OWN).transpose()
x5 = np.matrix(df2.Homeown_RENT).transpose()
x = np.column_stack([x1,x2,x3,x4,x5])

X = sm.add_constant(x)
model2 = sm.OLS(y,X)
f2 = model2.fit()
print(f2.summary())