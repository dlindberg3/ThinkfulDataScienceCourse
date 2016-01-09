import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import math

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace = True)
# loansData = pd.read_csv('loansData_clean.csv')
df = pd.DataFrame(loansData)

intrates = df['Interest.Rate'].map(lambda x: round(float(x.strip('%')), 4))
loanlength = df['Loan.Length'].map(lambda x: int(x.strip(' months')))
FICOscores = df['FICO.Range'].map(lambda x: x.split("-"))
FICOscore1 = FICOscores.map(lambda x: int(x[0]))
FICOscore2 = FICOscores.map(lambda x: int(x[1]))
df['Interest.Rate'] = intrates
df['Loan.Length'] = loanlength
df['FICO.Score'] = FICOscore1

# df.to_csv('loansData_clean.csv', header=True, index=False)

df['IR_TF'] = df['Interest.Rate'].map(lambda x: 0 if x < 12 else 1)
df['Intercept'] = 1
ind_vars = ['Intercept', 'FICO.Score', 'Amount.Requested']

logit_model = sm.Logit(df['IR_TF'], df[ind_vars])
logit_result = logit_model.fit()
coeff = logit_result.params

def logistic_function(fico, loan, coef):
	if type(fico) == int:
		exp_i = np.dot(coef, [1, fico, loan])
		prob_return = 1 / (1 + np.exp(-exp_i))
	else:
		prob_return = [None] * len(fico)
		for i in range(0,len(fico)):
			exp_i = np.dot(coef, [1, fico[i], loan[i]])
			prob_return[i] = 1 / (1 + np.exp(exp_i))
	
	return prob_return

fico_x = range(550, 950)
loan_x = np.repeat(10000, len(fico_x))
prob_y = logistic_function(fico_x, loan_x, coeff)

plt.figure()
plt.plot(fico_x, prob_y)
plt.ylabel('Probability of getting 12% loan')
plt.xlabel('FICO Score')
plt.show()