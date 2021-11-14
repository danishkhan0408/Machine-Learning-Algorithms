# regression using random forest

library(rpart)
library(randomForest)
library(caret) #to calculate SSE
library(ggplot2)#to plot the curve

filename = "C:/Users/Danish/Desktop/Data science/randomforest/energy_cooling_load_data.csv"
energy=read.csv(filename,header=T)
View(energy)
samples = floor(0.7*nrow(energy))
col_names=colnames(energy)[apply(energy,2,function(x)any(is.na(x)))]
col_names
energy$rel_comp=as.numeric(energy$rel_comp)
x=mean(energy$rel_comp)
print(x)
energy$rel_comp[is.na(energy$rel_comp)]=x
#View(energy)
energy$surf_area[is.na(energy$surf_area)]=mean(energy$surf_area)
energy$over_ht[is.na(energy$over_ht)]=mean(energy$over_ht)
t = sample(seq(1:nrow(energy)), samples,replace=F)
train = energy[t,]
lm_train=energy[t,c(-1,-3,-6,-8,-4)]

test = energy[-t,]

print(paste('train=',nrow(train),'test=',nrow(test)))

cols = colnames(train); cols
lencols = length(cols); lencols

# find the index of the y-variable
ndx = grep("cold_load",cols)

trainx = train[,1:ndx-1]
trainy = train[,ndx]
head(trainx)
head(trainy)

# linear regression model
# ------------------------
lm = lm(cold_load~., data=lm_train)
p1 = predict(lm,test)
length(p1)
summary(lm)
# decision tree regression model
# --------------------------------
dt1 = rpart(cold_load~., data=train, method="anova", 
            cp=0.01, minsplit=2, maxdepth=5)
p2 = predict(dt1,test)
length(p2)
summary(dt1)
# random forest regression model
# -------------------------------
rf1 = randomForest(trainx, trainy,mtry=3, ntree=50)
p3 = predict(rf1, test)
length(p3)

# build a dataframe with results of all 3 regression models
df1=data.frame("actual"=test$cold_load, 
               "linear_regr"=p1,
               "dt_regr"=p2,
               "rf_regr"=p3)
View(df1)

e1 = round(RMSE(df1$actual, df1$linear_regr),3)
e2 = round(RMSE(df1$actual, df1$dt_regr),3)
e3 = round(RMSE(df1$actual, df1$rf_regr),3)
cat(paste("RMSE comparison chart", "\n", 
          "Linear Regression:", e1, "\n", 
          "Decision Tree:", e2, "\n", 
          "Random Forest:", e3   ))

# plot the 3 graphs

# Linear Regression
ggplot(test, aes(test$cold_load, p1)) + geom_point(colour="green") + geom_smooth(colour="red",method=lm)+ggtitle("Actual vs Linear Regression")

# Decision Tree
ggplot(test, aes(test$cold_load, p2)) + geom_point(colour="black") + geom_smooth(colour="red",method=lm)+ggtitle("Actual vs Random Forest")

# Random Forest
ggplot(test, aes(test$cold_load, p3)) + geom_point(colour="blue") + geom_smooth(colour="red",method=lm)+ggtitle("Actual vs Random Forest")

