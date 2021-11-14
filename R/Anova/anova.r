path="C:/Users/Danish/Desktop/Data science/linear reg/tips.csv"
tips=data.frame(read.csv(path,header=T))
View(tips)
str(tips)

tot=nrow(tips)
samp=sample(seq(1:tot),floor(0.8*tot))
train=tips[samp,]
test=tips[-samp,]

head(train)

colnames(train)

#using linear regression
lm_reg=lm(tipamt~tips,data=train)
pred_lr=predict(lm_reg)
summary(lm_reg)

#using decision trees
#anova is used for linear regression using Decision tree
#class is used for classification using Decision tree
lm_dt=rpart(tipamt~tips,data=train,method="anova")
pred_dt=predict(lm_dt)
# create a data frame to compare the tip amt values of both the models and the actual amount
# Linear reg predicts better than the decision tree model
# Decision tree (anova) is not prefered for linear data sets/predictions
