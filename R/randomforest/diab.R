# random forest algorithm - CLASSIFICATION
# diabetes dataset
# This example of Diabetes performs a Classification

#install.packages("randomForest")

library(randomForest)
library(caret) # for confusion matrix

# Diabetes dataset to predict the patient is diabetic or not
path="C:/Users/Danish/Desktop/Data science/randomforest/diab.csv"
diab = read.csv(path, header=T)

head(diab)
View(diab)
nrow(diab)

diab$class=NULL

# do the mandatory data check here..NULL/Blanks/Outliers etc..

# split the dataset into Training and Testing
set.seed(456)
ind = sample(seq_len(nrow(diab)), floor(nrow(diab)*0.7)   )
train = diab[ind,]
test = diab[-ind,]

nrow(train)
nrow(test)

# negative --> no diabetes
# positive --> has diabetes

# to check the count of each value of a factor variable against the Y-variable
# ----------------------------------------------------------------------------
100*prop.table(table(train$class_val))

colnames(train)

# this is the correct way to call the randomforest() for Classification
# ---------------------------------------------------------------------
train_x = train[,1:8] #selecting columns 1 to 8
train_y = train[,9] #selecting column 9 only

colnames(train)
colnames(train_x)
head(train_y)

# ntree: number of trees, default value is 500
# mtry: number of random features(columns) in each tree
basemodel = randomForest(train_x, factor(train_y),mtry=3, ntree=150)
basemodel
table(train_y)

attributes(basemodel)
basemodel$confusion

# predict the Classification for the Testing data
# ------------------------------------------------
basepredictions1 = predict(basemodel, test)
confusionMatrix(test$class_val,basepredictions1,positive="positive")
table(test$class_val)
# 2nd method to call predict()
# -----------------------------
basepredictions2 = predict(basemodel, test[,1:8])
confusionMatrix(test$class_val,basepredictions2,positive="positive")


# plot the ROC curve. Only for bivariate classifications
# ------------------------------------------------------
library(ROCR)
oob.votes = predict(basemodel, test, type="prob")
# summary(oob.votes)

# positive only
# --------------
oob.pred = oob.votes[,2]
pred.obj = prediction(oob.pred,test[,9])
rp.perf = performance(pred.obj, measure="tpr",x.measure="fpr")
plot(rp.perf)
abline(a=0, b=1)

# Error rate of Random Forest
# OOB error rate (Y-axis) vs Number of Trees (X-axis)
plot(basemodel)

# distribution of number of nodes for the trees in the model 
hist(treesize(basemodel),main="number of nodes for the trees",col="green")

# Feature selection
# importance of features/attributes.
# higher the value, more important it is
# used for feature selection to optimise other algorithm
# uses the MeanDecreaseGini
# -------------------------------------------------------------
importance(basemodel)

# variable importance - for feature selection
# measure purity of nodes at the end of the tree without each variable
varImpPlot(basemodel)

varImpPlot(basemodel, sort=T, n.var=5, main="Top variables")

# occurance of each variable(feature) to predict
# greater occurance, more significant
varUsed(basemodel)

### </Feature selection>