# Logistic regression to determine Breast disease
set.seed(3690)

#libraries
library(caret)
#install.packages("ROCR")
library(ROCR)

path="C:/Users/Danish/Desktop/Data science/log reg/benign.csv"
bbd = read.csv(path, header=T, stringsAsFactors = F)
head(bbd)
tail(bbd)

View(bbd)


# get the count and proportion of 1 and 0
table(bbd$diagnosis)
100*prop.table(table(bbd$diagnosis))   #calculate proportions

# convert features into factor variables wherever reqd
str(bbd)

# check for uniqueness and accordingly change datatypes
unique(bbd$degree)
bbd$degree = as.factor(bbd$degree)

unique(bbd$med_check)
bbd$med_check = as.factor(bbd$med_check)

unique(bbd$nlv)
#bbd$nlv = as.factor(bbd$nlv)

unique(bbd$mst)
bbd$mst = as.factor(bbd$mst)

unique(bbd$school)
#bbd$school = as.factor(bbd$school)

# y-variable has to be a factor
# ------------------------------
levels(bbd$diagnosis)
bbd$diagnosis = as.factor(bbd$diagnosis)

str(bbd)

View(bbd)
# split the data into training and testing data
# set.seed(12345)

# randomly shuffle the dataset and sample, not required
grp = runif(nrow(bbd))
bbd = bbd[order(grp),]

# identify Numeric, Character and Factor variables from the dataset
# chars = names(bbd)[sapply(bbd,is.character)]
facts = names(bbd)[sapply(bbd,is.factor)]
nums = names(bbd)[sapply(bbd,is.numeric)]

print(facts)
print(nums)
#creating seperate data sets for the factors and numeric data types
num_data = bbd[nums]
fact_data = bbd[facts]

nrow(num_data)
nrow(fact_data)
View(train)
train$school=NULL
test$school=NULL

# EDA on numeric data
# 1) 0, outlier and missing value check
library(ggplot2)
boxplot(train$stratum,horizontal = T)  #no outliers
# 2) multicollinearity



# split the data 
sampledata = sample(2, nrow(bbd), replace = T, prob = c(0.7,0.3))
train = bbd[sampledata==1,]
test = bbd[sampledata==2,]

# check whether the levels are same in both train and test
# levels_in_train == levels_in_test --> OK
# levels_in_train > levels_in_test --> OK
# levels_in_train < levels_in_test --> NOT OK (ERROR)

table(bbd$degree)

l_train = levels(factor(train$degreel))
l_test =  levels(factor(test$degree))

if (any(l_train!=l_test))
  print("factors dont match") else
    print("factors are OK")

#train$school=NULL; test$school=NULL

# logistic regression - build the model
#basemodel = glm(diagnosis~., data=train, binomial(link="logit"))
train$degree=NULL
basemodel = glm(diagnosis ~ med_check + agp1 + agmn + weight + aglp + mst, binomial(link="logit"),
                data=train)
#school valriable is removed, check for erorrs/singularities in school.

summary(basemodel)  #lower AIC -> better model, best way to checkis through confusion matrix
table(train$degree) #degree 0 is missing ie, rest are all dummy variables and degree 0 is the reference variable
# predict the Binary outcome for attrition_value
# type = "response" gives probabilities
basepredictions = predict(basemodel, test, type="response")
print(basepredictions[1:20])

# check the count to convert probabilites to 0/1
table(test$diagnosis)

cutpoint = 0.5
predictions = ifelse(basepredictions <=0.5, 0,1)
print(predictions[1:10])

# confusion matrix
# 1 --> positive class
#library(caret)
#install.packages("e1071")
library(e1071)
confusionMatrix(as.factor(test$diagnosis), as.factor(predictions), positive="1")
table(test$diagnosis)  #to check the actual and predeicted values, here actual along y axis and predictions along x asxis
#library(ROCR)
preds = prediction(basepredictions,test$diagnosis)

# identifying the best cut-off by plotting the ROC curve
# 1) evaluations
# ------------------------------------
evals = performance(preds, "acc")
evals
plot(evals)
abline(h=0.85, v=0.65) # play with these values
max_yval = which.max(slot(evals, "y.values")[[1]])
max_acc = slot(evals, "y.values")[[1]][max_yval]
max_cutoff = slot(evals, "x.values")[[1]][max_yval]
print(paste("Best accuracy = ", round(max_acc,4), 
            " Best Cutoff = ", round(max_cutoff,4)))

predictions_max = ifelse(basepredictions <= max_cutoff, 0,1)
tab = table(predicted = predictions_max,actual = test$diagnosis)
confusionMatrix(as.factor(predictions_max),
                test$diagnosis, positive="1")

# plot ROC
perf = performance(preds, "tpr", "fpr")
plot(perf, colorize=T, main="ROC Curve", ylab = "Sensitivity", xlab = "1-Specificity")
abline(a=0, b=1)

# area under the curve (AUC)
auc = performance(preds, "auc")
round(unlist(slot(auc, "y.values")),3)


# feature selection technique
step(basemodel)