import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace = True)
df = pd.DataFrame(loansData)


plt.figure()
amtFunded_box = df.boxplot(column = ['Amount.Funded.By.Investors', 'Amount.Requested'])
plt.savefig("loan_boxplots.png")

plt.figure()
ax1 = plt.subplot(2,1,1)
df['Amount.Funded.By.Investors'].plot(kind = "hist")
ax1.set_title("Amount Funded By Investors")
ax1.set_xlim(0, 35000)
ax2 = plt.subplot(2,1,2)
df['Amount.Requested'].plot(kind = "hist")
ax2.set_title("Amount Requested")
ax2.set_xlim(0, 35000)
plt.savefig("loan_histograms.png")

plt.figure()
ax1 = plt.subplot(2,1,1)
stats.probplot(df['Amount.Funded.By.Investors'], dist = "norm", plot = plt)
ax1.set_title("Amount Funded By Investors")
ax2 = plt.subplot(2,1,2)
stats.probplot(df['Amount.Requested'], dist = "norm", plot = plt)
ax2.set_title("Amount Requested")
plt.savefig("loan_qqplots.png")

'''
plt.figure()
amtFunded_qq = stats.probplot(df['Amount.Funded.By.Investors'], dist = "norm", plot = plt)
plt.savefig("amtFunded_qqplot.png")

plt.figure()
amtFunded_hist = df.hist(column = 'Amount.Requested')
plt.savefig("amtRequested_histogram.png")

plt.figure()
amtFunded_qq = stats.probplot(df['Amount.Requested'], dist = "norm", plot = plt)
plt.savefig("amtRequested_qqplot.png")
'''