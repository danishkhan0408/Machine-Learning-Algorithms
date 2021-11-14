library(corrplot)
library(caret)
#install.packages("ISLR")
library(ISLR)
#dataset= market
#type = classification
market=Smarket

#View(market)
colnames(market)
str(market)
#check for multicollinearity
corr=cor(market[,1:8])
corrplot(corr,method="number",type="lower")
#remove the feature Year
market$Year=NULL
corr=cor(market[,1:7])
corrplot(corr,method="number",type="lower")

#split the data into train and test data
tot=nrow(market)
s=sample(seq(1,tot),0.7*tot)
train=market[s,]
test=market[-s,]
print(paste("Train ",nrow(train),"Test ",nrow(test)))

#build the LDA model with all features
m1=lda(Direction~.,data=train)
summary(m1)
print(m1)

prop.table(table(train$Direction))
p1=predict(m1,test)$class
confusionMatrix(test$Direction,factor(p1))
