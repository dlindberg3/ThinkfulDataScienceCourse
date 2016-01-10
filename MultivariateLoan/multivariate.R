# Multivariate Analysis
loan.data <- read.csv('LoanStats3a.csv')

attach(loan.data)

loan.data.sub1 <- loan.data[,c('int_rate','annual_inc','home_ownership')]
loan.data.sub1 <- loan.data.sub1[complete.cases(loan.data.sub1),]


X.data <- loan.data.sub1[,c('annual_inc','home_ownership')]
Y.data <- sub("%","",loan.data.sub1[,'int_rate'])

summary(lm(Y.data ~ X.data[,c('annual_inc')]))
summary(lm(Y.data ~ X.data[,c('annual_inc')] + factor(X.data[,c('home_ownership')])))
