from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

print("")
print("Performing the Chi-Square goodness of fit test")
print("H0: The data is uniformly distributed vs. H1: The data is not uniformly distributed")

alpha = 0.05 # Level of significance

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace = True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

plt.figure()
plt.bar(freq.keys(), freq.values(), width = 1)
plt.savefig('loan_credit_hist.png')

chi, p = stats.chisquare(freq.values())
print("")
print("The chi-square statistic is " + str(round(chi, 2)) + " and p-value is " + str(round(p, 2)))

if p < alpha:
	print("We reject the null hypothesis that the data is uniformly distributed and conclude that it does not follow a uniform distribution")
else:
	print("We fail to reject the null hypothesis that the data is uniformly distributed")

print("")