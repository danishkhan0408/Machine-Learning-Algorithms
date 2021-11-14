# Linear Regression
# dataset: Concrete
# Y: CCS (to predict the concrete strength)
#install.packages("car")
# load the libraries
library(car) # vif()
library(DAAG) # library for CV
library(caret) # classification and regression trg
library(corrplot) # correlation plot

# input file (.CSV)
path = "C:/Users/Danish/Desktop/Data science/linear reg/concrete.csv"
conc = read.csv(path,header=T)

head(conc)
View(conc)
rows=nrow(conc)
cols=length(colnames(conc))

paste("Rows = ", as.character(rows), ", Columns = ", as.character(cols))
View(conc)

# randomly shuffling the dataset
grp = runif(nrow(conc))
conc = conc[order(grp),]

# check for Nulls           dataset,columnwise,check for nulls
col_name = colnames(conc) [apply(conc, 2, function(n) any(is.na(n)))]
if(length(col_name) > 0) print("NULLs present") else print("No NULLs")

# check for Blanks
col_name = colnames(conc) [apply(conc, 2, function(n) any(n == ""))]
if(length(col_name) > 0) print("Blanks present") else print("No Blanks")

# check for 0
col_name = colnames(conc) [apply(conc, 2, function(n) any(n==0))]
if(length(col_name) > 0)
{
  print("Zeroes present in columns : ")
  print(col_name)
} else 
  print("No Zeroes")


# check for outliers individually for each column
# 1) boxplot
boxplot(conc$cementcomp,horizontal = T)
summary(conc$cementcomp)

boxplot(conc$slag,horizontal = T)
boxplot(conc$flyash,horizontal = T)
boxplot(conc$age)


# 2) histograms
hist(conc$cementcomp,breaks=20,col=rgb(1,0,1),main="Cement Composition")

# check for multicollinearity (correlation among the x-variables)
cor = cor(conc[1:8]) # gives values
corrplot(cor,method="number",type="lower")
#use variance inflation factor (vif) 
#if multicollinearity chart doesnt give a clear result. VIF>5 should be removed
# split the data into training and testing data
sampledata = sample(2, nrow(conc), replace = T, prob = c(0.7,0.3))
train = conc[sampledata==1,]
test = conc[sampledata==2,]

View(train)
View(test)

# total rows
nrow(train); nrow(test)

##### Model building process #####
##### ---------------------------- 
# fit the regression model

# model 1 with all variables
# lm(y-variable ~ glass + superplastisizer + water)

# formula = Y ~ .    ALL x VARIABLES
#          Y ~ x1+x2+x3 ONLY 3 X VARIABLES

basemodel = lm(CCS ~ ., data=train)
summary(basemodel)

# check the assumptions of the linear model
# ---------------------------------------------
# 1) parameters are linear

# 2) residuals mean is 0
mean(basemodel$residuals)

# 3) residuals have constant variance
# par(mfrow=c(2,2))
plot(basemodel)
# Plot 1: residuals vs fitted plot
# Along the x-axis, the fitted values for residuals increase and then
# decrease. (as shown by the red line). 
# It should be approximately flat

# Similar plot is Plot 3: scale-location
# Y-values are standardized values

# 4) residuals are normally distributed
#  Plot 2: Normal Q-Q
# It should be overall a straight line along the diagonal
# deviations along the two ends are expected
# Also indicates outliers

# 4) x-variables and residuals are not related
cor.test(train$cementcomp,basemodel$residuals)

# 5) Number of observations > Number of X's
dim(conc)

# 6) Variability of X-values is +ve
# var(conc$cementcomp)
# var(conc$slag)
# sqrt(10921.58)

##### end of assumptions checking. Stop here to correct data points


# variance inflation factor
# to check Multicollinearity
vif(basemodel)

# r-square value
r2 = summary(basemodel)$r.squared

# adjusted r2
# 1 - ((1-r2)(n-1) / n-p-1)
n = nrow(train); print(n)
p = length(colnames(train))-1; print(p)

1-(1-r2)*(n-1)/(n-p-1)

# cross-validation to check the best fit model
# 1)  which one to use ?
# a) this is the correct usage
# m --> indicates the number of folds
cv_basemodel = cv.lm(data=train, basemodel, m=3)

cv_basemodel$Predicted

# predicted values to check actual Y vs predicted Y of the model
cv_basemodel$cvpred

# predict the CCS with all the X-values
basemodel_predictions = predict(basemodel, test)
length(basemodel_predictions)

# table showing the difference between the actual and predicted values
df_results = data.frame("actual" = test$CCS, 
                   "predicted" = basemodel_predictions,
                   "difference" = test$CCS-basemodel_predictions)
df_results$sq_difference = df_results$difference^2
View(df_results)

print(paste("basemodel: Mean Square Error = ",mean(df_results$sq_difference)))

### build the next model using less X-variables. Repeat this and build
# multiple models and select the best

# relative importance of the variables in the model
# Use as a feature selection
# install.packages("relaimpo") realtive importance
library("relaimpo")

relimp1 = calc.relimp(basemodel, type="lmg")
variables = as.data.frame(relimp1$lmg)
print(variables)

# print the relative importance
barplot(relimp1$lmg, ylab="Relative importance", 
        xlab="Variables",
        main="Relative importance of x-variables")


# model 2 : with only the important variables
# ..........
# ..........
