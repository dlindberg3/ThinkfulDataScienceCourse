Written By:			David Lindberg
Date:				12/29/2015
Data Source: 		https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv
Description:		Lending Club Loan Amount Box Plots, Histograms, and QQ Plots

Side by side box plots, histograms, and QQ plots were generated for the Lending Club's loan amounts requested, and loan amounts funded by investors.  The following similarities and differences were noted:

Similarities:
	1) The median amount requested and funded by investors is $10,000.  The first quantile for each is $6,000, and the third quantile is about $17,000.
	2) Each data set is skewed right.
	3) Neither follows a normal distribution
	4) Each has an R-squared of approximately 0.93
	5) Each has a maximum of $35,000

Differences:
	1) There are more outliers within the amount funded by investors compared to the amount requested
	2) $0 is one of the amounts funded by investors, but not an amount requested

It would be worthwhile to perform a linear regression to assess how well correlated the two variables are.