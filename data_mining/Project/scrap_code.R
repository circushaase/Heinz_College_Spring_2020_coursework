#Scrap code

library("Hmisc")
library(corrplot)
library("PerformanceAnalytics")
library(dplyr)
library(ggplot2)


noncorrdata = housingClean[,c("AGE1", "REGION", "FMR", "BEDRMS", "BUILT", "NUNITS", "PER", "UTILITY", "OTHERCOST", "BURDEN", "APLMED", "INCRELAMIPCT", "COSTMedRELAMIPCT", "MOBILEHOME", "URBAN")]

chart.Correlation(noncorrdata, histogram=TRUE, pch=19)


# Age vs Monthly Housing Cost (COSTMedRELAMIPCT)

ggplot(data = housingClean, mapping=aes(x=AGE1  , y=COSTMedRELAMIPCT )) + geom_point() + geom_smooth(method = 'lm', color = 'red') +
  facet_wrap('FMTASSISTED') +
  labs(x = 'Age' , y = 'Housing cost at Median interest, Relative to Median Income (Percent)')


ggplot(housingClean, aes(MOBILEHOME, fill = FMTASSISTED)) + geom_histogram(binwidth = 0.1, position = "fill")

ggplot(housingClean, aes(FMTZADEQ, fill = FMTASSISTED)) + geom_histogram(binwidth = 1, position = "fill", stat="count")

confusion <- table(noncorrdata$FMTZADEQ, noncorrdata$FMTASSISTED)
#confusion



df = noncorrdata[which(noncorrdata$INCRELAMIPCT < 500),]
ggplot(df, aes(INCRELAMIPCT, fill = FMTZADEQ)) + geom_density(alpha=0.5)

ggplot(noncorrdata, aes(URBAN, fill = FMTASSISTED)) + geom_density(alpha=0.5)

#In an urban context, people who have more income, spend more on housing
ggplot(data = housingClean, mapping=aes(x=INCRELAMIPCT , y=COSTMedRELAMIPCT )) + geom_point() + geom_smooth(method = 'lm', color = 'red') +
  facet_wrap('URBAN') +
  labs(x ='Household Income relative to AMI (percent)' , y = 'Housing cost at Median interest, Relative to Median Income (Percent)', title = 'Household Income vs Housing Cost, by "Urban"')

